import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from pyspark.sql import SparkSession
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.clustering import LDA
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType
import numpy as np
import pandas as pd

stopword_remover = StopWordRemoverFactory().create_stop_word_remover()
stemmer = StemmerFactory().create_stemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', str(text))
    text = stopword_remover.remove(text)
    text = stemmer.stem(text)
    tokens = text.split()
    
    return tokens

# Create Spark Session
spark = SparkSession.builder \
    .appName("Latent Dirichlet Allocation Algorithm") \
    .getOrCreate()

# Read dataset
dataset = "hdfs://hadoop-namenode:8020/input/hasil_berita_detik_sport.csv"
df = spark.read.csv(dataset, header=True, inferSchema=True)
print("Dataset Schema:")
df.show()

df = df.drop('No')

df_cleaned = df.dropna(how='any')
df_cleaned = df_cleaned.filter(~df_cleaned["Pengarang"].contains("Pengarang tidak ditemukan"))
print("Cleaned Dataset Schema:")
df_cleaned.show()

# Create UDF for preprocessing
preprocess_udf = udf(preprocess_text, ArrayType(StringType()))

# Apply preprocessing
processed_df = df_cleaned.withColumn(
    "processed_tokens", 
    preprocess_udf(df_cleaned["Isi Berita"])
)


vectorizer = CountVectorizer(
    inputCol="processed_tokens", 
    outputCol="features", 
    vocabSize=10000,  
    minDF=5
)

vectorizer_model = vectorizer.fit(processed_df)
feature_data = vectorizer_model.transform(processed_df)

vocabulary = vectorizer_model.vocabulary
num_topics = 5 
max_iterations = 100

lda = LDA(k=num_topics, maxIter=max_iterations, featuresCol="features")
lda_model = lda.fit(feature_data)

def get_top_words_for_topics(lda_model, vocabulary, num_top_words=10):

    topics = lda_model.describeTopics(maxTermsPerTopic=num_top_words)
    
    topic_summaries = []
    
    for topic in topics.collect():
        term_indices = topic['termIndices']
        term_weights = topic['termWeights']
        
        topic_words = [(vocabulary[idx], weight) for idx, weight in zip(term_indices, term_weights)]
        topic_summaries.append(topic_words)
    
    return topic_summaries

# Print top words for each topic
print("Top Words for Each Topic:")
topic_words = get_top_words_for_topics(lda_model, vocabulary)
for i, topic in enumerate(topic_words):
    print(f"Topic {i + 1}:")
    for word, weight in topic:
        print(f"  {word} (weight: {weight:.4f})")
    print()

log_likelihood = lda_model.logLikelihood(feature_data)
print(f"Log-Likelihood: {log_likelihood}")

perplexity = lda_model.logPerplexity(feature_data)
print(f"Perplexity: {perplexity}")

topic_distributions = lda_model.transform(feature_data)
topic_dist_df = topic_distributions.select("topicDistribution")

avg_topic_weights = topic_dist_df.rdd.map(lambda row: np.array(row.topicDistribution)).mean()
print("\nAverage Topic Weights:")
for i, weight in enumerate(avg_topic_weights):
    print(f"Topic {i + 1}: {weight:.4f}")

# Optional: Save topic words to CSV for further analysis
topic_words_df = pd.DataFrame(
    [(i+1, word, weight) for i, topic in enumerate(topic_words) for word, weight in topic], 
    columns=['Topic', 'Word', 'Weight']
)
topic_words_df.to_csv('topic_words.csv', index=False)

# Stop Spark Session
spark.stop()
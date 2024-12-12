# Spark ML Project

This project demonstrates various machine learning models and data processing techniques using Apache Spark.

## Project Structure

```
docker-compose.yml
hdfs/
    input/
    output/
put_file.py
read_file.py
README.md
spark_code/
    lda.py
requirements.txt
```

## Setup

1. **Install Dependencies**: Ensure you have Python and the required libraries installed. You can install the dependencies using pip:
    ```sh
    pip install -r requirements.txt
    ```

2. **Start HDFS and Spark**: Use `docker-compose` to start HDFS and Spark services.
    ```sh
    docker-compose up
    ```

## Scripts

### Data Handling

- **Upload a file to HDFS**: Use [`put_file.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FBigData-Project%2Fput_file.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22f9fbdf57-544e-432c-90cc-f6f3dc5a6e67%22%5D "/workspaces/BigData-Project/put_file.py") to upload a file to HDFS.
    ```sh
    python put_file.py
    ```

- **Read a file from HDFS**: Use [`read_file.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FBigData-Project%2Fread_file.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22f9fbdf57-544e-432c-90cc-f6f3dc5a6e67%22%5D "/workspaces/BigData-Project/read_file.py") to read a file from HDFS.
    ```sh
    python read_file.py
    ```

### Lateng Dirichlet Allocation Models

- **Latent Dirichlet Allocation**: Train and test a LDA model using [`spark_code/lda.py`].
    ```sh
    python spark_code/lda.py
    ```

## HDFS Structure

- **Input Directory**: Place input files in [`hdfs/input/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FBigData-Project%2Fhdfs%2Finput%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22f9fbdf57-544e-432c-90cc-f6f3dc5a6e67%22%5D "/workspaces/BigData-Project/hdfs/input/").
- **Output Directory**: Output files will be saved in [`hdfs/output/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FBigData-Project%2Fhdfs%2Foutput%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22f9fbdf57-544e-432c-90cc-f6f3dc5a6e67%22%5D "/workspaces/BigData-Project/hdfs/output/").


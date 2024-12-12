from hdfs import InsecureClient

# Connect to HDFS Namenode
client = InsecureClient('http://localhost:8020', user='root')

# Reading a file from HDFS
with client.read('/hdfs/path/file.csv') as reader:
    data = reader.read()
    print(data)

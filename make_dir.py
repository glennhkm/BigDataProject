from hdfs import InsecureClient

# Connect to HDFS
client = InsecureClient('http://localhost:8020', user='root')

# Create a directory on HDFS
client.makedirs('/user/input/')
print("Directory successfully created!")


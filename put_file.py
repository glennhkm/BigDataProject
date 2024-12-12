from hdfs import InsecureClient
from hdfs.util import HdfsError
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    # Connect to HDFS
    client = InsecureClient('http://172.18.0.2:8020', user='root')

    # Upload a file to HDFS
    client.upload('/user/input/', './hdfs/input/hasil_berita_detik_sport.csv')
    print("File uploaded successfully!")
except HdfsError as e:
    print(f"An error occurred: {e}")

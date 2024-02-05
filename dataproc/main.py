# File: dataproc/main.py
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("DataProcessingJob") \
        .getOrCreate()

    # Your data processing logic here

    spark.stop()


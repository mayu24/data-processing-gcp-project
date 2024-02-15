from pyspark.sql import SparkSession

try:
    # Create a SparkSession with the BigQuery connector
    spark = SparkSession.builder \
        .appName("Merge Banking Data with Spark SQL") \
         .enableHiveSupport() \
        .getOrCreate()

    print("Spark Configurations:")
    for conf in spark.sparkContext.getConf().getAll():
        print(conf)

    # Define the SQL query to process the banking data
    sql_query = """
    INSERT INTO  `root-rock-413418.transactions_data.amounts` 
    SELECT *
    FROM `root-rock-413418.transactions_data.transactions`
    WHERE amount = 100; 
    """

    # Execute the SQL query
    spark.sql(sql_query)

    print("Data insertion completed successfully.")

except Exception as e:
    print("Error:", e)

finally:
    # Stop the SparkSession
    spark.stop()



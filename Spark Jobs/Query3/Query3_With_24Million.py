#!/usr/bin/env python
# coding: utf-8

from pyspark.sql import SparkSession
from sparkmeasure import StageMetrics

# Initialize Spark session
spark = SparkSession.builder.appName("MyApp").getOrCreate()
stagemetrics = StageMetrics(spark)



# Reading the CSV file without limit on number of records read. Storing the data in Spark DataFrame
taxi_df = spark.read.csv("hdfs:///data/2020_Yellow_Taxi_Trip_Data_20231129.csv", header=True, inferSchema=True)

# Create a temporary view of the dataframe
taxi_df.createOrReplaceTempView("taxi_data")

# Query to fetch trips with same pickUp and dropOff location
sql_query = """
SELECT a.*
FROM taxi_data a
JOIN taxi_data b ON a.PULocationID = b.DOLocationID
WHERE a.trip_distance < 1.0
"""

# Start measuring performance
stagemetrics.begin()

#Execute the query
result_df = spark.sql(sql_query)
result_df.show()

# Stop measuring performance
stagemetrics.end()

# Print the performance report
stagemetrics.print_report()
#!/usr/bin/env python
# coding: utf-8

from pyspark.sql import SparkSession
from sparkmeasure import StageMetrics

# Initialize Spark session
spark = SparkSession.builder.appName("MyApp").getOrCreate()
stagemetrics = StageMetrics(spark)


# Reading the CSV file with limit on number of records read. Storing the data in Spark DataFrame
taxi_df = spark.read.csv("hdfs:///data/2020_Yellow_Taxi_Trip_Data_20231129.csv", header=True, inferSchema=True).limit(5000000)

#Creating temporary view of the Dataframe
taxi_df.createOrReplaceTempView("taxi_data")

#Query to Fetch Average Fare Amount by Passenger Count
sql_query = """
SELECT passenger_count, AVG(fare_amount) AS average_fare
FROM taxi_data
GROUP BY passenger_count
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
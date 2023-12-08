#!/usr/bin/env python
# coding: utf-8

from pyspark.sql import SparkSession
from sparkmeasure import StageMetrics
from pyspark.sql.functions import col, when

# Initialize Spark session
spark = SparkSession.builder.appName("MyApp").getOrCreate()
stagemetrics = StageMetrics(spark)



# Reading the CSV file with limit on number of records read. Storing the data in Spark DataFrame
taxi_df = spark.read.csv("hdfs:///data/2020_Yellow_Taxi_Trip_Data_20231129.csv", header=True, inferSchema=True).limit(5000000)


# Start measuring performance
stagemetrics.begin()

#increase the fare_amount by 30% for trips with more than 2 passengers.
updated_df = taxi_df.withColumn("fare_amount",
                                when(col("passenger_count") > 2, col("fare_amount") * 1.3)
                                .otherwise(col("fare_amount")))
updated_df.show(10)

# Stop measuring performance
stagemetrics.end()

# Print the performance report
stagemetrics.print_report()
# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql import functions as F


data = [
(1, "Ravi", "Hyderabad", 25),
(2, None, "Chennai", 32),
(None, "Arun", "Hyderabad", 28),
(4, "Meena", None, 30),
(4, "Meena", None, 30),
(5, "John", "Bangalore", -5)
]
columns = ["customer_id", "name", "city", "age"]
df = spark.createDataFrame(data, columns)



## Identify data issues (nulls, duplicates, invalid values)
df.show()

## Count before performing cleaning
print(df.count())

##  Clean data 
## remove null keys
df_clean =df.dropna(subset=["customer_id"])
df_clean.show()

## handle missing values
df_clean = df_clean.fillna({"name":"unknown","city":"unknown"})
df_clean.show()


## remove duplicates
df_clean = df_clean.dropDuplicates()
df_clean.show()


## filter invalid age
df_clean = df_clean.filter(df.age >= 0)
df_clean.show()

## Validate cleaning
# Before cleaning
print("Before cleaning" ,df.count())
# After cleaning
print("After cleaning" , df_clean.count())

##  Perform aggregation (customers per city)
df_clean.groupBy("city").agg(F.count("customer_id").alias("customer_count")).show()

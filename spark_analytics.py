# spark_analytics.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder.appName("SalesAnalytics").getOrCreate()

# Distributed dataset
data = [("Laptop",45000,50), ("Phone",32000,80),
        ("Tablet",28000,40), ("Pen",5000,200), ("Bag",12000,60)]

df = spark.createDataFrame(data, ["Product","Revenue","Units"])

# Distributed query
df.groupBy("Product") \
  .agg(sum("Revenue").alias("Total_Revenue"),
       avg("Units").alias("Avg_Units")) \
  .orderBy("Total_Revenue", ascending=False) \
  .show()
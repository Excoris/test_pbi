# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "ccf70ee9-126c-4eeb-9107-89226077b927",
# META       "default_lakehouse_name": "Dp700",
# META       "default_lakehouse_workspace_id": "e7726c0f-dd6e-4b36-9268-6d99914ed121",
# META       "known_lakehouses": [
# META         {
# META           "id": "ccf70ee9-126c-4eeb-9107-89226077b927"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Sales order data exploration
# Use this notebook to explore sales order data


# CELL ********************


from pyspark.sql.types import *

orderSchema = StructType([
    StructField("SalesOrderNumber", StringType()),
    StructField("SalesOrderLineNumber", IntegerType()),
    StructField("OrderDate", DateType()),
    StructField("CustomerName", StringType()),
    StructField("Email", StringType()),
    StructField("Item", StringType()),
    StructField("Quantity", IntegerType()),
    StructField("UnitPrice", FloatType()),
    StructField("Tax", FloatType())
])

df = spark.read.format("csv").schema(orderSchema).load("Files/orders/*.csv")

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

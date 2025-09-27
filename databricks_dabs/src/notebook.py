# Databricks notebook source
# MAGIC %md
# MAGIC # Default notebook
# MAGIC
# MAGIC This default notebook is executed using Databricks Workflows as defined in resources/databricks_dabs.job.yml.

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

display(spark.read.table("samples.nyctaxi.trips"))

# COMMAND ----------

# MAGIC %md
# MAGIC - This is point 1
# MAGIC - This is point 2
# MAGIC

# COMMAND ----------



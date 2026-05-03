# Databricks notebook source
print("Starting Pipeline...")

# Bronze
dbutils.notebook.run("/Workspace/Repos/22pa1a1285@vishnu.edu.in/Banking-Transactions-Lakehouse-Project-Selected-Dataset-Edition/notebooks/bronze/bronze_load", 0)

# Silver
dbutils.notebook.run("/Workspace/Repos/22pa1a1285@vishnu.edu.in/Banking-Transactions-Lakehouse-Project-Selected-Dataset-Edition/notebooks/silver/silver_transform", 0)

# Gold
dbutils.notebook.run("/Workspace/Repos/22pa1a1285@vishnu.edu.in/Banking-Transactions-Lakehouse-Project-Selected-Dataset-Edition/notebooks/gold/gold_transform", 0)

print("Pipeline Completed Successfully!")
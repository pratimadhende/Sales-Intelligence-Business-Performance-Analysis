# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df=pd.read_csv(r"Superstore.csv", encoding="latin1")
print(df.head())

# understand the data
print(df.info())
print(df.describe())
print(df.isnull().sum())

# clean data 
# convert dates
df["Order Date"]=pd.to_datetime(df["Order Date"])
df["Ship Date"]=pd.to_datetime(df["Ship Date"])
# remove duplicates
df.drop_duplicates(inplace=True)
# clean column names 
df.columns = df.columns.str.replace(' ','_')
print(df.columns)

# feature Engineering
df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month
df["Order_Month_Name"] = df["Order_Date"].dt.month_name()
df["Order_Quarter"] = df["Order_Date"].dt.to_period("Q").astype(str)
df["Profile_Margin_%"] = (df["Profit"] / df["Sales"]) * 100 

# basic analysis
print(df.groupby("Category")["Sales"].sum())
print(df.groupby("Region")["Profit"].sum())
print(df.groupby("Segment")["Sales"].sum())

# save cleaned data 
df.to_csv("cleaned_superstore_data.csv",index=False)
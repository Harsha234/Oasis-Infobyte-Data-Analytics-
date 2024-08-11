#level 1 project 2 
#customer segmentation analysis 
#importing necessary libraries 
import numpy as np     
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("1.data collection \n")
# 1.data loading & cleaning 
file_path = 'C:/Users/rahul/OneDrive/Desktop/python/task-2/ifood_df.csv'
df = pd.read_csv(file_path)
print(df.head())

#printing all data columns 
print("checking all columns in our dataframe \n")
print(df.columns )
print("2.data exploration and cleaning \n ")
#2.data exploration and cleaning

#looking for missing value 
print("looking for missing value \n")
print(df.isna().sum())

#uniqueness
print("uniqueness \n")
print(df.nunique())

#Data Exploration

print("data exploration")
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, y='MntTotal')
plt.title('Box Plot for MntTotal')
plt.ylabel('MntTotal')
plt.show()
#Outliers

print("outliers")
Q1 = df['MntTotal'].quantile(0.25)
Q3 = df['MntTotal'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['MntTotal'] < lower_bound) | (df['MntTotal'] > upper_bound)]
print(outliers.head())




# 3.Calculate Average Purchase Value
print("3.Descriptive Statistics")
transactions = pd.DataFrame(df)
total_amount_spent = transactions['Income'].sum()
total_transactions = transactions.shape[0]
average_purchase_value = total_amount_spent / total_transactions

print("Average Purchase Value:", average_purchase_value)
#4.visualization
print("4.visualization")
#histogram for income
print("Hiotogram for income")
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Income', bins=30, kde=True)
plt.title('Histogram for Income')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()
     
#histogram for age
print("histogram for age")
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', bins=30, kde=True)
plt.title('Histogram for Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
     
#K-Means Clustering
print("5.k-means clustering")
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
cols_for_clustering = ['Income', 'MntTotal']
data_scaled = df.copy()
data_scaled[cols_for_clustering] = scaler.fit_transform(df[cols_for_clustering])   
print(data_scaled[cols_for_clustering].describe())

print("6.insights and recommendations")

print("1.We can Calculate the average purchase value by summing up all purchase amounts and dividing by the total number of transactions")
print("2.We can Visualize the distribution using histograms or box plots to identify any patterns or anomalies")
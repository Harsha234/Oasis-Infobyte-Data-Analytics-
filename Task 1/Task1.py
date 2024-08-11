
# level 1 --project 1 
#Exploratory Data Analysis (EDA) on Retail Sales Data
#importing necessary libraries 
import numpy as np     
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("1.data loading and cleaning")
#1. data loading & cleaning 
file_path = 'retail_sales_dataset.csv'
df = pd.read_csv(file_path)

# adjusting display options for our dataframe
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print("Last few rows of the dataframe:")
print(df.tail())
# displaying the  information about the dataframe 
print("\nDataFrame Info:")
df.info()

# printing the count of null values in each column for checking of completeness
print("\nnull counts for each column:")
print(df.isnull().sum())
print("Total sales : {}".format(df["Quantity"].sum()))
print("Total profit : {}".format(df["Total Amount"].sum()))
#for counting the no of duplicated rows in our dataframe 
print(df.duplicated().sum())




print("---------------------------------------------------------------------------------------------------------")
print("2.descriptive statistics")
#2.descriptive statistics
#it means numerical measures that summarize the main features of a dataset  (mean,median,mode,standard deviation, etc.)
print(df.describe())




print("---------------------------------------------------------------------------------------------------------")
print("3.time series analysis")
#3.time series analysis
# used to analyze data that is collected, recorded, or observed over time
print(sns.pairplot(df))
plt.show()




print("---------------------------------------------------------------------------------------------------------")
print("4.Customer and product analysis")
#4.Customer and product analysis
#here we are analyzing customer demographics and purchasing behavior.
print(df["Product Category"].value_counts())





print("---------------------------------------------------------------------------------------------------------")
print("5.Visualization")
#5.Visualization
#here we present  the insights through bar charts, line plots, and heatmaps
#bar graphs
sns.countplot(x=df["Product Category"])
plt.show()

#heat maps
sns.pairplot(df, hue="Product Category")
plt.show()

#printing piecharts
cate=df["Product Category"].value_counts()
explode_list=[0,0.1,0.1]
color_list=["Red","Blue","Seagreen"]
cate.plot(kind="pie", figsize=(15,6))
plt.title("Product Category")
plt.axis("equal")
plt.show()




print("---------------------------------------------------------------------------------------------------------")
print("recommendations")
#6.recommendations


print(" 1.We can analyze  the least performing product categories") 
print("  and consider some plans to improve their sales, such as marketing campaigns or product diversification. ")     
print("2.We can monitor changes in sales trends over time to identify upcoming market opportunities  according to  consumer preferences. ")   
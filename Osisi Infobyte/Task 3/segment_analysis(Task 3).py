#level 1 task3 
#segment analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import seaborn as sns

# Load the CSV file into a pandas DataFrame
data_duplicates = pd.read_csv('C:/Users/rahul/OneDrive/Desktop/python/task-3/apps.csv')

# Display the first few rows of the DataFrame
print("first few rows")
print(data_duplicates.head())
apps = data_duplicates.drop_duplicates()
print("Total numbers of Apps : ", apps[ 'App' ].count())
apps.head()



ch_remove = ('+' , '$' , 'M' , ',' )
col_clean = ('Size','Installs','Price')
for col in col_clean:
    for char in ch_remove:
        apps[col] = apps[col].str.replace(char, '')
    apps[col] = pd.to_numeric(apps[col])
n_categories = len(set(apps['Category']))
print('Number of categories = ', n_categories)
n_apps_in_category = apps['Category'].value_counts().sort_values(ascending=False)
data1 = go.Bar(
    x = n_apps_in_category.index,
    y = n_apps_in_category.values
)
fig = go.Figure(data1)
fig.show()



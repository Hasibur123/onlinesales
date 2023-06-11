import pandas as pd

df = pd.read_csv('data.csv')

# Sort the dataframe by average salary in descending order
sorted_df = df.sort_values('Avg_salary', ascending=False)

# Fetch the top 3 departments
top_3_departments = sorted_df.head(3)['DEPT_NAME']

# Print the top 3 departments
print(top_3_departments)
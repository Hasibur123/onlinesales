import pandas as pd

data = pd.read_csv('Data.csv')

# Calculate the average salary per department
avg_salary_per_dept = data.groupby('Name_of_department')['Total_amount_paid'].mean()

# Sort the departments by average salary in descending order
sorted_departments = avg_salary_per_dept.sort_values(ascending=False)

# Fetch the top 3 departments
top_3_departments = sorted_departments.head(3)

# Print the top 3 departments and their average salaries
print(top_3_departments)
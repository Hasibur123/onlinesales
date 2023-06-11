# onlinesales
solution 1:-
I made assumpution as only 2 colomn are given
Table name = Data
Assumption 1 :- Given colomn are (ID , DEPT_NAME , AVG_MONTHLY_SALARY)

QUERRY	:- SELECT DEPT_NAME, AVG_MONTHLY_SALARY FROM Data ORDER BY AVG_MONTHLY_SALARY DESC LIMIT 3;

Assumption 2 :- Given colomn are ( ID , DEPT_NAME , NO_OF_EMPLOYIES , TOTAL_AMOUNT_PAID )

QUERRY :- SELECT DEPT_NAME, (Total_amount_paid / No_of_employees) AS AVG_MONTHLY_SALARY
		FROM Data
		ORDER BY AVG_MONTHLY_SALARY DESC
		LIMIT 3;

solution 2:-

cssv file name = Data.csv

Assumption 1 :- Given colomn are (ID , DEPT_NAME , Avg_salary)
CODE :-
import pandas as pd

df = pd.read_csv('your_file.csv')

# Sort the dataframe by average salary in descending order
sorted_df = df.sort_values('Avg_salary', ascending=False)

# Fetch the top 3 departments
top_3_departments = sorted_df.head(3)['DEPT_NAME']

# Print the top 3 departments
print(top_3_departments)

Assumption 2 :- Given colomn are ( ID , DEPT_NAME , NO_OF_EMPLOYIES , TOTAL_AMOUNT_PAID )
CODE :-
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

solution 3

I have use python language
Here i found 2 mistakes

mistake 1 -> range(1,n-10) since range iritate one less to the second argument
		so need to take addition of 1 in required calculation.
mistake 2 -> formula for calculating sum of first n number is n*(n+1)/2 but here 
		uses n*(n-1)/2 , i made it correct


def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-9):
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        out = out + lim
        out = out / 2 
    print(out)
n = int(input("Enter an integer: "))
compute(n)

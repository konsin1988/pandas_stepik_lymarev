import pandas as pd 
import matplotlib.pyplot as plt 

empl = pd.read_parquet('../tables/employees.parquet')

print(empl['salary'].describe())

print(empl['salary'].agg(['mean', 'max', 'std'])['mean'].round(4))

marks = pd.read_csv('../tables/оценки 6Д.csv')

print(marks
    .drop(['ФИО', 'Пол'], axis=1)
    .agg(['mean', 'max', 'min'])
)

print(empl.query('report_dt == "2022-12-31"').sample(100, replace=True)['salary'].quantile(0.8))
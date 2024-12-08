import pandas as pd 

marks = pd.read_csv('../tables/оценки 6Д.csv')
list_names = ['fio', 'sex', 'math', 'russian', 'literature', 'phisics', 'history', 'sport']
marks = marks.rename(columns = dict(list(zip(marks.columns, list_names))))

print(marks
    .query('math == 4')
    .query('history > 3')
    [['fio', 'russian', 'phisics']]
)
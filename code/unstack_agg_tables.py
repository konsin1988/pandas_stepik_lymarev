import pandas as pd 
import numpy as np 

empl = pd.read_parquet('../tables/employees.parquet')

# unstack --------------------------------
print(
    empl
    .groupby(['report_dt', 'pos_name'])
    [['salary']]
    .mean()
    .round(2)
    .unstack('pos_name')
    .head(20)
)

# crosstab -------------------------------------
print(
    pd
    .crosstab(index=empl['report_dt'],
    columns = empl['pos_name'],
    values= empl['salary'],
    aggfunc='mean',
    dropna=True)
    .head(20)
)

# pivot_table сводная таблица ----------------------
print(
    empl
    .pivot_table(index='report_dt',
    columns = 'pos_name',
    values = 'salary',
    aggfunc = 'mean',
    margins = True)
    .round(2)
    .head(20)
)

# transform + groupby Добавление сводной колонки в датафрейм -------------- 
# Средняя зп по магазину и по позиции 
print(
    empl 
    .assign(mean_group_salary = lambda x: x
        .groupby(['report_dt', 'shop_id', 'pos_name'])
        ['salary']
        .transform('mean')
        .round(2))
    .iloc[:, [2, -2, -1]]
    .sample(10, random_state=10)
)
print()

# transform + groupby ----------------------------
# Колонка с разницей между средней зп 
# по группе и зп сотрудника
print(
    empl 
    .assign(mean_salary_diff = lambda x: x
        .groupby(['report_dt', 'shop_id', 'pos_name'])
        ['salary']
        .transform(lambda x: x - x.mean())
        .round(2)
    )
    .iloc[:, [1, 2, -2, -1]]
    .sample(20, random_state=100)
)
print()

# groupby + transform + join
# Добавить несколько аггрегационных колонок
print(
    empl 
    .join(
        empl
        .groupby(['report_dt', 'shop_id', 'pos_name'])
        [['employee_evaluation', 'salary']]
        .transform(lambda x: x - x.mean()
        .round(2)),
        rsuffix = '_cea')
    .iloc[:,[-4, -3, -2, -1]]
    .sample(20, random_state=13)
)
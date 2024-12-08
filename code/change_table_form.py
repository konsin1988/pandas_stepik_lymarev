import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 

empl = pd.read_parquet('../tables/employees.parquet')

empl_agg = ( empl
            .groupby(['report_dt', 'pos_name'])
            [['salary']]
            .mean()
            )

# print(empl_agg.head(20))

# Unstack, Перекидываем pos_name в шапку таблицы
print(empl_agg.unstack('pos_name'))

# pivot_table, the same as previous
unstacked = (empl_agg
      .reset_index()
      .pivot_table(columns='pos_name', index='report_dt')
      .head(20)
      )

# stack, "разложи по полочкам", обратная unstack
print(unstacked.stack('pos_name'))


# pivot_table with only one column        !!!!pivot_table only with groupby !!!!!
empl_agg_small = ( empl
            .groupby(['pos_name'])
            [['salary']]
            .mean()
            )
print(
    empl_agg_small
    # .unstack('pos_name')
    .reset_index()
    .pivot_table(columns='pos_name')
)

# melt 
marks = pd.read_excel('../tables/оценки.xlsx')
print(
    marks
    .drop('Пол', axis=1)                                # Удобно строить barplotё
    .melt(id_vars=['ФИО'])
    .set_index(['ФИО'])
    .query('variable.str.contains("Математика")')
    .reset_index()
    .set_index('variable')
    )

sns.barplot(marks.melt(value_vars=['Математика', 'Русский язык']), x='variable', y='value', estimator='std')
plt.show()


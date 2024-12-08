import pandas as pd
import matplotlib.pyplot as plt 

ltc = pd.read_parquet('../tables/ltc_sample.parquet')

# print(
#     ltc[['price']]
#     .sample(5, random_state=123)
#     .sort_index()
#     .assign(shift_1 = lambda x: x['price'].shift(1))
#     .assign(shift_2 = lambda x: x['price'].shift(2))
# )

# diff 
# print(
#     ltc[['price']]
#     .sample(5, random_state=123)
#     .sort_index()
#     .assign(diff = lambda x: x['price'].diff(1))
# )

# iris = pd.read_csv('../tables/iris.csv')

# print(iris.head())
# print(iris.head().assign(diff = lambda x: x[['Sepal.Width']].diff(1)))

# Прирост к предыдущему значению
# print(
#     ltc
#     .sample(5, random_state=123)
#     .sort_index()
#     .assign(pct_change = lambda x: x['price'].pct_change(1) * 100)
# )

# # Приведение к одной частоте
# print(
#     ltc
#     .drop_duplicates('date', keep='last')
#     .set_index('date')
#     .rename({pd.Timestamp('2013-11-13 15:00:56'): pd.Timestamp('2013-11-13 15:00')})
#     .asfreq(freq='1 d', method='ffill')
# )

# Статистики за равные промежутки времени RESAMPLE
# print(
#     ltc
#     .set_index('date')
#     .resample('1 d')
#     # ['price']
#     .mean()
# )

# Открытие, max, min, Закрытие
# First, max, min, last
# print(
#     ltc
#     .set_index('date')
#     .resample('1 d')
#     ['price']
#     # .ohlc()       # open, high, low, close
#     .agg(['mean', 'max'])
# )

stocks = pd.read_parquet('../tables/stocks.parquet')

# Среднее за каждое второе наблюдение
# print(
#     stocks
#     ['Цена']
#     .rolling(10, min_periods=1)
#     .agg(['max', lambda x: x[::2].mean()])
#     .set_axis(['Max_to_10', 'Mean for every two'], axis=1)

# )

# print(
#     stocks
#     .expanding().std()
# )

# print(
#     stocks
#     .ewm(alpha=0.5)
#     .mean()
# )


# --------------------------------------------------
#           HOME TASKS
#---------------------------------------------------
# Для каждого месяца посчитать отношения числа 
# проданных товаров в этом месяце к предыдущему, 
# а так же прирост в выручке

sales = pd.read_parquet('../tables/sales_sample.parquet')

# print(sales
#  .set_index('purchase_date')
#  [['price', 'goods_number']]
#  .assign(sum = lambda x: x['price'] * x['goods_number'])
#  .resample('1 m').sum()
#  .assign(goods_number_pct = lambda x: x['goods_number'].pct_change(1))
#  .assign(sum_diff = lambda x: x['sum'].diff(1))
#  [['goods_number_pct', 'sum_diff']]
# )

# Посчитать VaR и ES (на уровне 95%) для цены акций на 1 и на 10 торговых дней

# VaR (value at risk) (на уровне 95%) - 
# это 95 квантиль потерь (или пятый квантиль доходностей)

# ES (expected shortfall) (на уровне 95%) - 
# это средние убытки при условии, что состоялся 
# неблагоприятный сценарий и убытки пробили 95% порог


# -------------------------------------------------------------------
# Для каждого сотрудника посчитать среднюю оценку за 3 месяца и за полгода. 
# Предварительно приведите колонку с оценкой сотрудника к типу float
empl = pd.read_parquet('../tables/employees.parquet')

# print(
#     empl
#     .set_index('report_dt')
#     .groupby('fio')
#     [['employee_evaluation']]
#     .resample('3 M')
#     .mean()
#     .set_axis(['Mean 3 month'], axis=1)
#     .round(2)
#     .query('report_dt.dt.year == 2017')
# )
# ----------------------------------------------------------------
# Для каждого сотрудника почитайте его среднюю оценку 
# по состоянию на каждый месяц. То есть если сотрудник 
# пропаботал год, то для каждого месяца его работы должна 
# быть вычислена средняя оценки за предыдущие месяца его работы. 
# Предварительно приведите колонку с оценкой сотрудника к типу floats

# print(
#     empl
#     .set_index('report_dt')
#     .groupby('fio')
#     .expanding(min_periods=1)
#     [['employee_evaluation']]
#     .mean()
#     .set_axis(['mean_cum'], axis=1)
#     .assign(diff = lambda x: x.diff(1) > 0)
#     .groupby('fio')
#     ['diff']
# )

print(
    empl
    .assign(mean = lambda x: x.groupby('fio')[['employee_evaluation']].mean())
    [['employee_evaluation', 'mean']]
    # .set_index('report_dt')
    # .groupby('fio')
    # [['employee_evaluation']]
    # .expanding(min_periods=1)
    # .mean().round(2)
    # .set_axis(['mean_cum'], axis=1)
)
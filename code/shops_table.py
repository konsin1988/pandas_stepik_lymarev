import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../tables/shops.xlsx', index_col='shop_id')
df = df.astype({'city': 'string', 'adress': 'string', 'shopping_center': 'string', 'size': 'string'})
df.info()

empl = pd.read_parquet('../tables/employees.parquet')
empl['salary'] = empl['salary'].astype('int64')
empl.info()

xdg_usdt = pd.read_csv('../tables/XDGUSDT.csv', header=None).set_axis(['date', 'price', 'amount'], axis=1)
print(pd.to_datetime(xdg_usdt['date'], unit='s'))
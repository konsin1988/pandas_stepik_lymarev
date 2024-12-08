import pandas as pd 

sales = (pd.read_parquet('../tables/sales_2022.parquet')
    .assign(purchase_date = lambda x: x['purchase_date'].dt.normalize())
    .drop_duplicates(['customer_id', 'purchase_date'])
    .dropna()
)[['customer_id', 'purchase_date']]
# print(sales.head(20))
w_ends = (pd.read_csv('../tables/выходные.csv')
    .set_axis(['purchase_date', 'is_weekend'], axis=1)
    .assign(purchase_date = lambda x: x['purchase_date'].astype('datetime64[ns]'))
)
# print(w_ends.head(20))

print(sales.merge(w_ends, on='purchase_date').head(30))
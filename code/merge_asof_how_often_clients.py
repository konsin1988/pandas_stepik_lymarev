# Посчитаем с какой периодичнотью к нам в среднем ходят клиенты

import pandas as pd 

sales = pd.read_parquet('../tables/sales_2022.parquet')[['customer_id', 'purchase_date']]

print(pd.merge_asof(
    sales.rename(columns={'purchase_date':'purchase_date_first'}).dropna(), 
    sales.rename(columns={'purchase_date':'purchase_date_last'}).dropna(),
    left_on = 'purchase_date_first',
    right_on = 'purchase_date_last',
    by='customer_id',
    direction='forward',
    allow_exact_matches = False
    )
    .assign(time_interval = lambda x: (x['purchase_date_last'] - x['purchase_date_first']))[['customer_id', 'time_interval']].dropna().sort_values('time_interval', ascending=False)
    .head(30)
)


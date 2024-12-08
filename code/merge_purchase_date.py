import pandas as pd 

df = pd.read_parquet('../tables/sales_2022.parquet')
df = df[['customer_id', 'purchase_date']].drop_duplicates().reset_index(drop=True).dropna()

def come_backers(df, month):
    df_feb = (df
        .assign(purchase_month=lambda x: x['purchase_date'].dt.normalize() + pd.offsets.MonthEnd(0)-pd.offsets.MonthEnd(1))
        .drop_duplicates(['customer_id', 'purchase_month'])
        .query(f'purchase_month.dt.month == {month}')
        [['customer_id', 'purchase_month']]
        .assign(indicator = True)
    )
    df_ya = (df
        .assign(purchase_month=lambda x: x['purchase_date'].dt.normalize() + pd.offsets.MonthEnd(0))
        .drop_duplicates(['customer_id', 'purchase_month'])
        .query(f'purchase_month.dt.month == {month}')
        [['customer_id', 'purchase_month']]
    )
    # print(pd.concat([df_feb, df_ya])['customer_id'].duplicated().sum()/df_ya['customer_id'].count())
    return pd.merge(df_ya, df_feb, on=['customer_id', 'purchase_month'], how='left')['indicator'].notna().mul(100).mean().round(2)

print(come_backers(df, 1))
# print(come_backers(df, 6))


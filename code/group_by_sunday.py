import pandas as pd 
import numpy as np 

ltc = pd.read_parquet('../tables/ltc_sample.parquet')

print(
    (ltc[ltc['date'].dt.day_name() == 'Sunday'].groupby(by=ltc['date'].dt.date)['price'].agg(['mean'])).set_axis([ 'mean price'], axis=1))


# Все выходные, уникальные даты
print(ltc[(ltc['date'].dt.day_name() == 'Sunday') & ~ltc['date'].dt.date.duplicated()]['date'])
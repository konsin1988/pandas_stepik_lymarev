import pandas as pd 
import numpy as np 

ltc = pd.read_parquet('../tables/ltc_sample.parquet')

#  Точная информация по дате и времени
print(ltc
    .set_index('date')
    .asof('2017-03-30 23:05:00')
)


# Варианты запросов
print('----- with normalize()--------')
print( ltc
    .query('date.dt.normalize() == "2017-03-30"')       
    .head()
)
print('----------- with pd.Timestamp---------------------')
print(ltc[ltc['date'] == pd.Timestamp('2013-11-13 15:58:20')])
print('------------------------------------')
print(ltc.query('date > "2017-03-30"'))
print('---------asof--------------')
print(
    ltc
        .set_index('date')
        .asof('2014-11-02 00:03:25')
)

print(
    ltc
        .set_index('date')
        .at_time('12:00')
        .head()
)

print((ltc['date'][10000] - ltc['date'][10]))
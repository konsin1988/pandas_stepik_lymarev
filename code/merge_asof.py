import pandas as pd 

events = pd.read_parquet('../tables/events.parquet')[['i_pernr', 'date', 'event_type']]

# print(events.head(30))
hired = (
    events
        .query('event_type == "Прием на работу"')
)[['i_pernr', 'date']]
dissmiss = (
    events
        .query('event_type == "Увольнение"')
)[['i_pernr', 'date']]

print(hired.sort_values('i_pernr').head(10))
print(dissmiss.sort_values('i_pernr').head(10))
import pandas as pd

data={
    'day':['Monday','Tuesday','Wednesday','Thursday','Friday'],
    'date':['1-01-2001','02-01-2001','03-01-2001','04-01-2001','05-01-2001']
      }
dt=pd.DataFrame(data)
print(dt.shape)
print(dt.describe())

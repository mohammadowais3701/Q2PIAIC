import pandas as pd
import numpy as np
data = pd.Series(np.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'a',],
[1, 2, 3, 1, 2, 3, 1, 2, 2, 1]])
#print(data.index)
#print(data['b'])
#print(data['b':'c'])
#print(data.unstack())
#print(data.sort_index(level=0))
#print(data)
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=[['Ohio', 'Ohio', 'Colorado'],
['Green', 'Red', 'Green']])
#print(frame)
frame.index.names = ['key1', 'key2']
#print(frame)
frame.columns.names = ['state', 'color']
print(frame)
#print(frame['Ohio'])
#print(frame.swaplevel(0,1))
#print(frame.sort_index(level=0))
print(frame.sum(level='key2'))
print(frame.sum(level='color',axis=1))
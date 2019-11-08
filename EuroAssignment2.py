#import libraries
import pandas as pd
import numpy as np

#import csv files and assign into euro12
def get(k):
    k=np.array(k[1])

    for x in k:

       if x<=2:
         return 'Below Avg'
       elif (x>2 and x<=5):
        return "Average"
       elif (x>5 and x<=10):
        return "Above Average"
       elif (x>10):
        return "Excellent"



euro12=pd.read_csv('Euro_2012_stats_TEAM.csv')
print('Select only the Goal column')
print(euro12['Goals'])
print('How many team participated in the Euro2012')
print(len(euro12['Team']))
print('What is the number of columns in the dataset')
print(len(euro12.columns))
print('View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline')
discipline=pd.DataFrame(euro12['Team'][euro12['Yellow Cards'][ euro12['Red Cards']]])
print(discipline)
print('Sort the teams by Red Cards, then to Yellow Cards')
print(euro12.sort_values(by=['Red Cards','Yellow Cards'] ))
print('Calculate the mean Yellow Cards given per Team')
print(round(euro12['Yellow Cards'].mean()))
print('Filter teams that scored more than 6 goals')
print(euro12['Team'][euro12['Goals']>6])
print('Select the teams that start with G')
firstLetter=euro12['Team'].astype(str).str[0]
print(firstLetter)
print('Select the first 7 columns')
print(pd.DataFrame.head(euro12,7))

print('Select all columns except the last 3.')
print(euro12[euro12.columns[:-4]])

print(' Present only the Shooting Accuracy from England, Italy and Russia')
print(euro12['Shooting Accuracy'][euro12['Team'].isin(['England','Italy','Russia'] )])


print("Use apply method on Goal Column to make a new column called Performance, using following conditions")
print("If Goals are less than or equal to 2, peformance is Below Avg")
print("If Goals are more than 2 and less than or equal to 5, peformance is Average")
print("If Goals are more than 5 and less than or equal to 10, peformance is Above Average")
print("If Goals are more than 10 then peformance is Excellent")

euro12['Performance']=euro12.apply(lambda x: get(euro12['Goals']))


from itertools import count
import pandas as pd
from josaaanly.models import Data




df = pd.read_csv('../ORCR_16_22_all.csv')
df = df.rename(columns={'Opening Rank' : 'OpeningRank','Closing Rank' : 'ClosingRank','Seat Type' : 'SeatType','Academic Program Name':'Programme'})

df = df[[#'Unnamed: 0', 
    'Institute', 'Programme', 
    #'Quota',
    'SeatType', 'Gender' ,
    'OpeningRank', 'ClosingRank', 'Year', 'Round']].copy()

df['Gender'].fillna('Gender-Neutral')

dualDegDf = df['Programme'].apply(lambda x : pd.Series(x.split('(')))
dualDegDf = dualDegDf.rename(columns={0:'Branch',1:'DualDeg'})
dualDegDf = dualDegDf[['Branch','DualDeg']]
def isDual(x):
    if x[0] == '4':
        return False
    else:
        return True

dualDegDf.head()
dualDegDf['DualDeg'] = dualDegDf['DualDeg'].apply(lambda x: pd.Series(isDual(x)))
df['DualDeg'] = dualDegDf['DualDeg']
count =0
for index,row in df.iterrows():
    data_instance = Data(Institute=row['Institute'],Programme=row['Programme'],SeatType=row['SeatType'],Gender=row['Gender'],OpeningRank=row['OpeningRank'],ClosingRank=row['ClosingRank'],Round=row['Round'],DualDeg=row['DualDeg'],Year=row['Year'])
    data_instance.save()
    count +=1
    print(count)

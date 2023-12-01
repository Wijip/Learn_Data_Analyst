#Assignment
import pandas as pd
import numpy as np

data1 = np.array(['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'])
series = pd.Series(data1, index=[1,2,3,4,5,6,7,8,9,10,11,12])

print(series.loc[1:12])
print(series.iloc[0:12])
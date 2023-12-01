import pandas as pd
import numpy as np

data = np.array(['APPLE','ORANGE','BANANA','GRAPE','MANGO'])
frame = pd.DataFrame(data)
series = pd.Series(data)

print(f'Series : \n{series}\n')
print(f'Data Frame: \n{frame}')
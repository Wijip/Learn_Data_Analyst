import numpy as np

A = np.random.randint(100, 1000, size=(4,4))
print(f'No 1 = \n{A}\n')
print(f'No 2 = {A[A > 500]}\n')
print(f'No 3 = {A[(A > 200) & (A < 550)]}')
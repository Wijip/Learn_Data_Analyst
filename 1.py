import numpy as np

A = np.array([
    [1,'Januari', 4799],
    [2,'Februari', 3154],
    [3,'Maret', 4238],
    [4,'April', 2929],
    [5,'Mei', 1615]
])

B = np.array([
    [4779,3454,4799],
    [6533,4444,3154],
    [2939,2348,4238],
    [2355,4654,2929],
    [2342,5532,1615]
])

ko = A[...,2]
c = ko.astype(np.int32)
print(f'Nomor 1 = \n{A}\n')
print(f'Nomor 2 = {c.sum()}\n')
print(f'Nomor 3 = {c.mean()}\n')
print(f'Nomor 4 = {c*2.5}\n')
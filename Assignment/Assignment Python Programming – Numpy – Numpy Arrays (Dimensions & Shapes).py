import numpy as np

array1 = np.array([
    [10,20,30],
    [5,10,20],
    [2,4,6]
])

array2 = np.array([
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [20, 21, 22],
        [23, 24, 25],
        [26, 27, 28]
    ],
    [
        [30, 31, 32],
        [33, 34, 35],
        [36, 37, 38]
    ]
])

print(f'Array 2D = \n{array1}\n')
print(f'Array 3D = \n{array2}')
# print(array2.ndim)
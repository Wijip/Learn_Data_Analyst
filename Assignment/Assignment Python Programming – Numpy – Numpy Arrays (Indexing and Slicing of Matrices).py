import numpy as np

array = np.array([
    ['Denish','Scratch', 8],
    ['Frank','Python', 18],
    ['Roger','Unity', 15]
])

print("No. 2")
print(f'1. {array[0]}')
print(f'2. {array[1]}')
print(f'3. {array[2]}')

print("\nNo. 3")
print(f'4. \n{array[:,:2]}')

print("\nNo. 4")
array[0][1] = 'Roblox'
print(array)
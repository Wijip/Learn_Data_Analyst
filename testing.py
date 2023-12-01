#Assignment
import pandas as pd

data = pd.Series([408, 943, 902, 117, 389, 435, 793, 356, 651, 993, 786, 157], index=['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'])
tambah = pd.Series([408, 943, 902, 117, 389, 435, 793, 356, 651, 993, 786, 157], index=['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'])
print(f'No 1:\n{data}\n')
average = data.mean()
print(f'No 2:\n{average}\n')
print(f'No 3:\n{data[data > average]}')
ganti = average.astype(int)
replace = data[data > ganti] = ganti
print(f'\nNo 3.1:\n{data}')
print(f'\nNo 4.1:\n{data.add(tambah, fill_value=0)}')
print(f'\nNo 4.2:\n{data.subtract(tambah, fill_value=0)}')

# ganti = data.replace()

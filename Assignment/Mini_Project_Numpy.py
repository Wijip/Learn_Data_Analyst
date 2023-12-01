import numpy as np

def hitung(matrix1, matrix2):
    matrix_jumlah = matrix1 + matrix2

    sum_matrix_1 = matrix1.sum()
    mean_matrix_1 = matrix1.mean()
    standart_deviasi_matrix_1 = matrix1.std()
    sum_matrix_2 = matrix2.sum()
    mean_matrix_2 = matrix2.mean()
    standart_deviasi_matrix_2 = matrix2.std()

    return matrix_jumlah, sum_matrix_1, mean_matrix_1, standart_deviasi_matrix_1, sum_matrix_2, mean_matrix_2, standart_deviasi_matrix_2

matrix1 = np.array([1,2,3,4,5])
matrix2 = np.array([6,7,8,9,10])

matrix_jumlah, sum_matrix_1, sum_matrix_2, mean_matrix_1, mean_matrix_2,standart_deviasi_matrix_1, standart_deviasi_matrix_2 = hitung(matrix1, matrix2)

print(f'Matrix Jumlah = {matrix_jumlah}')
print(f'Sum Matrix 1  = {sum_matrix_1}')
print(f'Mean Matrix 1 = {mean_matrix_1}')
print(f'Standar Deviasi Matrix 1 = {standart_deviasi_matrix_1}')
print(f'Sum Matrix 1  = {sum_matrix_2}')
print(f'Mean Matrix 1 = {mean_matrix_2}')
print(f'Standar Deviasi Matrix 1 = {standart_deviasi_matrix_2}')
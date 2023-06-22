my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
new_list = my_list
print(my_list, new_list, sep='\n')

my_list[2] = 555
print(my_list, new_list, sep='\n')



my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')

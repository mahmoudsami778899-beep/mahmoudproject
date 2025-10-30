
import numpy as np 

A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

add_result = A + B           
sub_result = A - B          
mul_result = A * B          
div_result = A / B           

mean_A = np.mean(A)         
max_A = np.max(A)           
min_A = np.min(A)            
dot_product = np.dot(A, B)  
reshaped_A = A.reshape(5, 1) 

print(" A:", A)
print(" B:", B)
print("A + B =", add_result)
print("A - B =", sub_result)
print("A * B =", mul_result)
print("A / B =", div_result)
print("mean of A:", mean_A)
print("max of A:", max_A)
print("min of A:", min_A)
print("dot product of A and B:", dot_product)
print("reshaped A (5x1):", reshaped_A)

import pandas as pd 
students_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [20, 22, 19, 21, 20],
    'grade': ['A', 'B', 'A', 'C', 'B'],
    'marks': [85, 78, 92, 65, 74]
})

print("first 3 rows:")
print(students_data.head(3))

print("name and ,arks columns:")
print(students_data[['name', 'marks']])

print("students with grade A:")
print(students_data[students_data['grade'] == 'A'])

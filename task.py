
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

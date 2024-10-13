# Asking the user for the dimension of the matrix
#print("Insert size of array: ")
n = int(input())
if n <= 0:
    print("BŁĄD")

# Creating an empty matrix
matrix = []

# Filling the matrix with zeros using nested loops
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)  
    matrix.append(row)  

# Print the matrix 
for i in range(n):
    for j in range(n):
        if j == n - 1:  
            print(matrix[i][j], end="")  # No space after the last element
        else:
            print(matrix[i][j], end=" ") 
    print()  
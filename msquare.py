# Define a function to split a matrix into four submatrices
def split(matrix):
    # Get the size of the matrix
    n = len(matrix)

    # Get the midpoint of the matrix
    mid = n // 2

    # Initialize the submatrices
    split_matrix_a = [[0 for j in range(mid)] for i in range(mid)]
    split_matrix_b = [[0 for j in range(mid)] for i in range(mid)]
    split_matrix_c = [[0 for j in range(mid)] for i in range(mid)]
    split_matrix_d = [[0 for j in range(mid)] for i in range(mid)]

    # Copy the values from the original matrix to the submatrices
    for i in range(mid):
        for j in range(mid):
            split_matrix_a[i][j] = matrix[i][j]
            split_matrix_b[i][j] = matrix[i][mid + j]
            split_matrix_c[i][j] = matrix[mid + i][j]
            split_matrix_d[i][j] = matrix[mid + i][mid + j]
    return split_matrix_a, split_matrix_b, split_matrix_c, split_matrix_d


# Define a function to add two matrices
def add(matrix1, matrix2):
    # Get the size of the matrices
    n = len(matrix1)

    # Initialize the result matrix
    result = [[0 for j in range(n)] for i in range(n)]

    # Add the corresponding elements of the matrices
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result


# Define a function to subtract two matrices
def subtract(matrix1, matrix2):
    # Get the size of the matrices
    n = len(matrix1)

    # Initialize the result matrix
    result = [[0 for j in range(n)] for i in range(n)]

    # Subtract the corresponding elements of the matrices
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result


# Define a function to join four submatrices into one matrix
def join(split_matrix_a, split_matrix_b, split_matrix_c, split_matrix_d):
    # Get the size of the submatrices
    n = len(split_matrix_a)

    # Initialize the result matrix
    result = [[0 for j in range(2 * n)] for i in range(2 * n)]

    # Copy the values from the submatrices to the result matrix
    for i in range(n):
        for j in range(n):
            result[i][j] = split_matrix_a[i][j]
            result[i][j + n] = split_matrix_b[i][j]
            result[i + n][j] = split_matrix_c[i][j]
            result[i + n][j + n] = split_matrix_d[i][j]
    return result


# Define a function to multiply two matrices using Strassen algorithm
def strassen(matrix_1, matrix2, explanation=None):
    # Get the size of the matrices
    n = len(matrix_1)

    # Base case: if the size is 1, return the product of the single elements
    if n == 1:
        return [[matrix_1[0][0] * matrix2[0][0]]]

        # Initialize the explanation if not provided
    if explanation is None:
        explanation = []

    # Recursive case: split the matrices into four submatrices
    split_matrix_a, split_matrix_b, split_matrix_c, split_matrix_d = split(matrix_1)
    split_matrix_e, split_matrix_f, split_matrix_g, split_matrix_h = split(matrix2)

    # Compute the seven products using the Strassen formula
    product_1 = strassen(split_matrix_a, subtract(split_matrix_f, split_matrix_h))
    product_2 = strassen(add(split_matrix_a, split_matrix_b), split_matrix_h)
    product_3 = strassen(add(split_matrix_c, split_matrix_d), split_matrix_e)
    product_4 = strassen(split_matrix_d, subtract(split_matrix_g, split_matrix_e))
    product_5 = strassen(add(split_matrix_a, split_matrix_d), add(split_matrix_e, split_matrix_h))
    product_6 = strassen(subtract(split_matrix_b, split_matrix_d), add(split_matrix_g, split_matrix_h))
    product_7 = strassen(subtract(split_matrix_a, split_matrix_c), add(split_matrix_e, split_matrix_f))

    # Compute the four submatrices of the result matrix
    sub_matrix_1 = subtract(add(add(product_5, product_4), product_6), product_2)
    sub_matrix_2 = add(product_1, product_2)
    sub_matrix_3 = add(product_3, product_4)
    sub_matrix_4 = subtract(subtract(add(product_5, product_1), product_3), product_7)

    # Join the submatrices into one matrix
    result = join(sub_matrix_1, sub_matrix_2, sub_matrix_3, sub_matrix_4)

    explanation.append({
      'Matrix_1': matrix_1,
      'Matrix_2': matrix2,
      'Step_Products': {
        'Product_1': product_1,
        'Product_2': product_2,
        'Product_3': product_3,
        'Product_4': product_4,
        'Product_5': product_5,
        'Product_6': product_6,
        'Product_7': product_7,
      },
      'Submatrices_Result': {
        'Sub_Matrix_1': sub_matrix_1,
        'Sub_Matrix_2': sub_matrix_2,
        'Sub_Matrix_3': sub_matrix_3,
        'Sub_Matrix_4': sub_matrix_4,
      },
      'Result_Matrix': result
    })

    return result

# Example usage:
matrix_1 = [[1, 2], [3, 4]]
matrix_2 = [[5, 6], [7, 8]]
explanation = []

result = strassen(matrix_1, matrix_2, explanation)

# Print the step-by-step explanation
for step, info in enumerate(explanation, start=1):
    print(f"Step {step}:")
    print(f"Matrix 1:\n{info['Matrix_1']}")
    print(f"Matrix 2:\n{info['Matrix_2']}")
    print("Step Products:")
    for product_name, product_matrix in info['Step_Products'].items():
        print(f"{product_name}:\n{product_matrix}")
    print("Submatrices Result:")
    for sub_matrix_name, sub_matrix in info['Submatrices_Result'].items():
        print(f"{sub_matrix_name}:\n{sub_matrix}")
    print(f"Result Matrix:\n{info['Result_Matrix']}\n")
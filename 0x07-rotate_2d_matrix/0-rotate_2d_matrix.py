#!/usr/bin/python3
"""
Rotate 2D Matrix module.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix by 90 degrees clockwise in place.
    
    Args:
        matrix (list of lists): The 2D matrix to rotate.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row to get the 90-degree rotation
    for i in range(n):
        matrix[i].reverse()


#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
  """
    Rotate 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix: The input 2D matrix to be rotated.

    Returns:
        None: The function modifies the input matrix in-place.
    """
  n = len(matrix)

  # Transpose the matrix in-place
  for i in range(n):
      for j in range(i + 1, n):
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  # Reverse each row in-place
  for i in range(n):
      matrix[i].reverse()

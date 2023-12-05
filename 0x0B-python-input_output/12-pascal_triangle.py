#!/usr/bin/python3
"""Pascal’s triangle of n:"""


def pascal_triangle(n=5):
    """Pascal’s triangle of n:"""
    if n <= 0:
        return

    triangle = []

    i = 0
    for i in range(n):
        row = []
        for j in range(i + 1):
            # print(f"[{i}][{j}]", end="")
            if i == 0 and j == 0:
                row.append(1)
            elif j - 1 < 0:
                row.append(triangle[i - 1][0])
            elif j >= len(triangle):
                row.append(triangle[i-1][j - 1])
            else:
                row.append(triangle[i-1][j - 1] + triangle[i-1][j])
        triangle.append(row)

    return triangle

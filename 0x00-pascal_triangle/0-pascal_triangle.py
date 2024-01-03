#!/usr/bin/python3
""" 0-pascal_triangle """


def pascal_triangle(n):
    """
    returns list of integers representing thw pascal triangle of n
    args:
        n - interger
        Returns an empty list if n <= 0 or pascal triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                # Calculate the value based on the values from the previous row
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        triangle.append(row)

    return triangle

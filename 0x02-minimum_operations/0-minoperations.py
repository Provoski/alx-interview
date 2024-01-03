#!/usr/bin/python3
'''0-minoperations.py module'''


def minOperations(n):
    '''
    minOperations - calculates the fewest number of
    operations needed to result in exactly n H characters
    in the file.
    args:
        n - given number
    return - 0 if impossible or an integer
    '''

    if n < 1:
        return 0

    '''
    Initialize an array to store the minimum operations
    for each position
    '''
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    '''
    Iterate from 2 to n to calculate minimum operations
    '''
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

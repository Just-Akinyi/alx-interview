#!/usr/bin/python3
'''defines minOperations function'''
def minOperations(n: int) -> int:
    '''calculates the fewest number of operations needed'''
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        operations += 1
        if n % i == 0:
            n /= i
        else:
            i += 1
    return operations + 1

#!/usr/bin/python3
'''
Module for calculating the minimum number of oprations
needed to result in exaclty  n H characters in a file
'''

def minOperations(n):
    """
    calculates the fewest number of operations needed to result in 
    n H characters in the file

    :param n: the target number of H characters
    : type n: int
    :return: The minimum number of operations or 
    if n is impossible to achieve
    :rtype: int
    """
    # if n is less than 1, return 0
    if n <= 1:
        return 0

    #initializa  operation and facor
    operation = 0
    factor = 2

    #repeat the task if n is greater than 1
    while n > 1:
        #repeat doing it , if n is divisible by factor
        while n % factor == 0:
            # add operation by factor to get minimum number
            operation += factor
            # divide n by factor to reduce n
            n //= factor
        # if n is not fdivisible by factor, lets increase facor
        factor += 1

    # return sum of operation, which is minimum num we want
    return operation


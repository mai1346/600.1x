# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:17:39 2018

@author: mai13
"""
#%% Problem 3
def count7(N):
    '''
    N: a non-negative integer'''
    if N//10==0:
        if N==7:
            return 1
        else:
            return 0
    else:
        return count7(N//10)+count7(N%10)
    
count7(17345677)
#%% Problem 4
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    product=[]
    for i in range(len(listA)):
        product.append(listA[i]*listB[i])
    return sum(product)
a = [1, 2, 3]
b = [4, 5, 6]
dotProduct(a,b)
#%% Problem 5
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    import operator
    #get frequencies of dictionary values
    valueFreq={}
    for value in aDict.values():
        valueFreq[value]=valueFreq.get(value,0)+1
    #get the list of keys with values only appear once 
    keyvaluelist=[]
    for key in valueFreq.keys():
        if valueFreq[key]==1:
            keyvaluelist.append(key)
    keylist=[]
    for akey in aDict.keys():
        for letter in keyvaluelist:
            if aDict[akey]==letter:
                keylist.append(akey)

    #sort keylist in increasing order
    return sorted(keylist)
#%% Problem 6
def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if b==0:
        return a
    else:
        return gcd(b,a%b)
gcd(20,12)
#%% Problem 7
def f(s):
    return 'a' in s
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
#    ml=[]
#    for i in L:
#        if f(i):
#            ml.append(i)
#    for i in range(len(L)-1):
#        if f(L[i]):
#            L[i],L[i+1]=L[i+1],L[i]
#    for i in range(len(L)-len(ml)):
#        L.pop(0)
#    print(L)
#    return len(ml)
    for i in L[:]:
        if not f(i):
            L.remove(i)
    return len(L)

L = ['a', 'b',  'a','c','d','e','b', 'b', 'b', 'b', 'b','a']
print (satisfiesF(L))
print (L)
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:24:25 2018

@author: mai13
"""

s='abcacbaaaaaaaaaaaaaaa'
a=[]
i=0
order=s[0]
while i<len(s)-1:
    if s[i]<s[i+1]:
        order+=s[i+1]
    else:
        a.append(order)
        order=s[i+1]
    i+=1
a.append(order)
print(a)
y=0
x=0
while x<len(a):
    if len(a[x])>len(a[y]):
        y=x
    x+=1
print (a[y])       
        
#b={x:len(x) for x in a}
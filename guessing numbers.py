# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:05:58 2018

@author: mai13
"""
#%%
low=0
high=100
print('Please think of a number between 0 and 100!')
print('Is your secret number 50?')
answer=''
while answer !='c':
    answer=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer=='h':
        high=int((low+high)/2)
        print('Is your secret number',str(int((low+high)/2))+'?')
    elif answer=='l':
        low=int((low+high)/2)
        print('Is your secret number',str(int((low+high)/2))+'?')
    elif answer=='c':
        print('Game over. Your secret number was:',int((low+high)/2))   
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number',str(int((low+high)/2))+'?')

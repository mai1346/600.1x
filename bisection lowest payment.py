# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:45:41 2018

@author: mai13
"""
#%%
def Rbalance(balance,annualInterestRate,monthlyPaymentRate,m=12): 
    if m<1:
        mbalance=balance
    else:
        mbalance=Rbalance(balance,annualInterestRate,monthlyPaymentRate,m-1)*(1-monthlyPaymentRate)*(1+annualInterestRate/12)
    return round(mbalance,2)
Rbalance(balance,annualInterestRate,monthlyPaymentRate,m=12)
#%%
balance = 999999
annualInterestRate = 0.18

lbound=balance/12
ubound=balance*(1+annualInterestRate/12)**12/12
temp=balance

while abs(balance)>0:

    balance=temp
    payment=(lbound+ubound)/2
    for i in range(12):
        balance=(balance-payment)*(1+annualInterestRate/12)
    if balance>0.01:        
        lbound=(lbound+ubound)/2
#        payment=(lbound+ubound)/2
    elif balance<-0.01:
        ubound=(lbound+ubound)/2
    else:
        print('Lowest Payment:',round(payment,2))
        break


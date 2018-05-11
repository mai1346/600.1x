# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:13:25 2018

@author: mai13
"""
#%% Problem 3
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for a in range(n//6+1):
        for b in range(n//9+1):
            for c in range(n//20+1):
                if 6*a+b*9+c*20==n:
                    print(a,b,c)
                    return True                    
    else:
        return False

#%% Problem 4
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    freq={}
    for num in L:
        freq[num]=freq.get(num,0)+1
    print(freq) 
    largest=max(freq.keys())
    while True:
        if freq[largest]%2!=0:
            return largest
            break
        else:
            del freq[largest]
            if len(freq.keys())==0:
                return None
            else:
                largest=max(freq.keys())            
a=[2,2,3,3]
largest_odd_times(a)
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
aDict = {}
uniqueValues(aDict)
#%% Problem 6
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name +' says: It is obvious that ' + Person.say(self,stuff)
    def lecture(self,stuff):
        return 'It is obvious that '+ Person.say(self,stuff)
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

#%% Problem 7
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        try:
            self.vals[e]-=1  
        except:
            self.vals[e]=0

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        if e in self.vals.keys():
            return self.vals[e]
        else:
            return 0











#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:46 2018

@author: agatakaczmarek
"""
#%%
def linear(num,list2):
        for i in range (len (list2)):
            if num==list2[i]:
                return True
    
        return False
#%%
def hello ():
    name = input("What is your name?")
    print ("hello" + name)

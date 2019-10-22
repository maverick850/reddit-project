# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:46:31 2019

@author: BenE
"""

'''configure settings'''
posneg = "pos","neg"
sorts = "best","top","controversial","new"
postdata = "Date","Post ID","Title","username","URL"


'''following variables are user controls'''
postdataindex = (1,2,3,4)

sortsindex = (5,11,17,23)
posnegindex = (7,9,13,15,19,21,25,27),(8,10,14,16,20,22,26,28)

keylist = list()

for i in range(len(postdata)):
    choice = input("would you like include",str(postdata[i]),"?")
    if choice == 'y' or "Y":
        keylist.extend(postdataindex[i])

for i in range(len(sorts)):
    choice = input("would you like to sort by:",sorts[i],"?")
    if choice == 'y' or "Y":
        keylist.extend(sortsindex[i])
        
for i in range(len(posneg)):
    choice = input("would you like to sort by:",posneg[i],"?")
    if choice == 'y' or "Y":
        keylist.extend(posnegindex[i])

keylist.sorted(reverse = True)

print(keylist)
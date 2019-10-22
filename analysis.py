# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:03:37 2019

@author: BenE
"""
def keycreator:
    '''configure settings'''
    posneg = ("pos","neg")
    sorts = ("best","top","controversial","new")
    postdata = ("Date","Post ID","Title","username","URL")

    
    '''following variables are user controls'''
    postdataindex = (1,2,3,4)

    sortsindex = (5,11,17,23)
    posnegindex = (7,9,13,15,19,21,25,27),(8,10,14,16,20,22,26,28)
    
    keylist = list()
    
    for i in range(len(postdata)):
        choice = input("would you like include",postdata[i],"?")
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

import posturldata

def prepinfovisual(postinfolist):
    
    keylist = keycreator()
    
    print (len(postinfolist))
    
    weeks = list()
    weekkey = list()

    postbyweek = list()
    templist = list()
    
    '''extract week from each post'''
    for post in postinfolist:
        weeks.append(post[0][1])
    print("list of weeks:",weeks)
    
    '''creates a list of numbers of posts per week'''
    from itertools import groupby
    weekkey = ([len(list(group)) for key, group in groupby(weeks)])
    print("Number of post per week:",weekkey)
    
    '''creates list of posts for each week in timespan'''
    postindex = 0
    for i in weekkey:
        
        for x in range(i):
            templist.append(postinfolist[postindex])
            postindex += 1
        postbyweek.append(templist)
        templist = list()
    
    
    """
    KEYS to PostInfo:
    date,post ID,title,username,url,numcomments,BEST,postotal,negtotal
    0 = date
    1= post ID
    2 = title
    3 = username
    4 = url
    
    5 = numcomments
    6 = sort:BEST
    7 = pos total
    8 = neg total
    9 = pos words
    10 = neg words
    
    11 = numcomments
    12 = sort:TOP
    13 = pos total
    14 = neg total
    15 = pos words
    16 = neg words
    
    17 = numcomments
    18 = sort: CONTROVERSIAL
    19 = pos total
    20 = neg total
    21 = pos words
    22 = neg words
    
    23 = numcomments
    24 = sort:NEW
    25 = pos total
    26 = neg total
    27 = pos words
    28 = neg words
    29 = dictionary of the number of times each site linked
    
    """

    '''These are the keys of info you want to sum'''
#    listofkeys = (6,7,8,9,10,13,14,15,16,19,20,21,22,25,26,27,28)
    #listofkeys = (8,9,11,12,16,17,21,22)
    
    listofkeys = (9,10)
    templist = list()
#    count = 0
    
    '''Calculate number of time each website is visited per week'''
    urldict = posturldata.main(postbyweek)
    print("000000000000000000000000\n",urldict)
    
    for key in listofkeys:
        
        '''iterate through weeks'''
        for week in range(len(postbyweek)):
            '''iterate post in week'''
            curweek = postbyweek[week]
            
            
            print (curweek,'\n\n\n\n')
#            numpostinweek = len(curweek)
#            print(numpostinweek)
            '''skips week if there is only 1 post'''
            if len(curweek) == 1:
                continue
#            curweek.append(numpostinweek)
            '''add the dictionaries of each week'''
            for post in range(len(curweek)):
                for k,v in curweek[post][key].items():
                    if k in curweek[0][key].keys():
                        curweek[0][key][k] += v
                    else:
                        curweek[0][key].get(k,v)
    
    ''' ADD HERE?keys for finding the average number of coments per sort type per week'''
    
    '''This takes the summed data and filters results'''
    splitforgraph = list()                          
    for week in postbyweek:
        x = week[0]
        
        '''put our selection here'''
        selection = (x[0],x[6],x[7:12])
        splitforgraph.append(selection)
        
    for week in splitforgraph:
        print(week)
        
    
    '''Print out results'''
#    splitforweek = posturldata.main(splitforweek)
    return splitforgraph

#def main():
##    sorts = ("best","top","controversial","new")
#    listofkeys = (6,7,8,9,10,13,14,15,16,19,20,21,22,25,26,27,28)
#    
#    splitforgraph = prepinfovisual(postinfolist,listofkeys)
#    
#    for week in splitforgraph:
#            print('\n\n',week,'\n\n')
#            
#    return splitforgraph


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
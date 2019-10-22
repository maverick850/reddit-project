# -*- coding: utf-8 -*-

'''Merges words from all posts into one dictionary'''
def dictmerger(wordlist,c,cursort,merge):
    curid = c+cursort
    '''check if sort id in merge'''
    if curid not in merge.keys():
        merge[curid] = wordlist
    else:    
        '''iterates words'''
        for k,v in wordlist.items():
            '''check if word is in merge'''
            if k in merge[curid].keys():
                merge[curid][k] = merge[curid][k]+v   
            else:
                merge[curid][k] = v                

    return (merge)

''''dictionary of number of comments by sort type'''   
def countcomments(c,cursort,totalcomments,numcomments): 
    curid = c+cursort
    if curid not in totalcomments.keys():
        totalcomments[curid] = numcomments
    else:
        totalcomments[curid] += numcomments
    return (totalcomments)

'''calculates the average word complexity'''
def wordcomplexity(length,words):
    complexity = 0
    for k,v in words.items():
        complexity += len(k)*v
    return (complexity/length)


'''Turns a wordlist into list and sorts it'''
def wordsorter(wordlist,cut):
    lst = list()
    for itempair in wordlist.items():
        lst.append(itempair)
    lst.sort(key = lambda x: x[1], reverse = True)
    if cut == 'Y':
        lst = lst[:10]
    lst = dict(lst)
        
    
    return lst
'''Takes the list of posts and formats by week for bar graphs'''
def splitpostsbyweek(postlist):
    
    weeks = list()
    weekkey = list()
    postbyweek = list()
    templist = list()
    
    for x in range(len(postlist)):
        weeks.append(postlist[x][0][1])
    
    from itertools import groupby
    weekkey = ([len(list(group)) for key, group in groupby(weeks)])
    
    postindex = 0
    
    '''iterates through number of seuential weeks, splits the weeklist into weeks'''
    for i in weekkey:
        for x in range(i):
            templist.append(postlist[postindex])
            postindex += 1
        postbyweek.append(templist)
        templist = list()
#    for post in postbyweek:
#        for x in post:
#            print(x[0][1])
            
    return postlist
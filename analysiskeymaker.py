def main():


"""
KEYS to PostInfo:
bestkeys = [5:11]
bestsummed = [7:11]

contkeys = [17:23]
contsummed = [15:23]

newkeys = [23:29]
newsummed = [25:29]

keys added
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

"""
'''These are the keys of info you want to sum'''

'''
I need to change the database format so all entries are dictionaries
 so they can be dynamically referenced using only the name
'''

for i in range(len(postinfolist[0])):

    x = week[0]
    time = x[0]
    username = x[3]
    url = x[4]
    totalcomments = x[5]
    
    best = x[5],x[6],x[8],x[7],x[9]
    bestsort = x[5]
    bestpostot = x[6]
    bestnegtot = x[7]
    bestpos = x[8]
    bestneg = x[9]
    
    top = x[10],x[11],x[13],x[12],[14]
    topsort = x[10]
    toppostot = x[11]
    topnegtot = x[12]
    toppos = x[13]
    topneg = x[14]
    
    cont = x[15],x[16],x[18],x[17],x[19]
    contsort = x[15]
    contpostot = x[16]
    contnegtot = x[17]
    contpos = x[18]
    contneg = x[19]
    
    new = x[20],x[21],x[23],x[22],[24]
    newsort = x[20]
    newpostot = x[21]
    newnegtot = x[22]
    newpos = x[23]
    newneg = x[24]
    
    
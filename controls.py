'''TO START PROGRAM ENTER SETTINGS AND RUN THIS FILE'''

'''following variables are user controls'''

subredditname = "politics"
posttimeframe = "month"
'''number of post that are search for the searchterm. Final number of post will be fewer'''
numberofposts = 10
replacelimit = 0
searchterm = "Trump"
cut = 'N'
cutafter = "Y"

comsort = "best"

sortbytime = "Y"
aggregate = 'N'

posneg = ("pos","neg")
sorts = ("best","top","controversial","new")

'''Select data to compare'''
gatherdata = input("Hello user. Would you like to scrape data?\n'Y'/'N'\n->")

if gatherdata == "Y":
    import scraping
    print("-> Scraping enitiated")
    ''''pass settings to scraper'''
    scraping.main(posneg,sorts,sortbytime,cut,searchterm,aggregate,replacelimit,subredditname,posttimeframe,numberofposts)

analyse = input("Would you like to analyse data?\n'Y'/'N'\n->")    

if analyse == 'Y':
    import analysis
    import fetchdataset
    print("-> Fetching data...")
    postinfolist = fetchdataset.main()
    print("->Done fetching...")
    
    settings = input(print("would you like to change analysis criteria?"))
    if settings == "Y":
        import keymaker
        listofkeys = keymaker.main()
    
    print("->Analysing data...")
    splitforgraph = analysis.prepinfovisual(postinfolist)
    print("->Done analysing data...")
    quit
    


    

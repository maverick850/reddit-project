import ast

def main():
    import os
    

    print ("Select file:")
    
    '''Path where datasets are stored'''  
    path = r"C:\Users\BenE\Desktop\Python\Projects\reddit project\datasets"
    
    '''Gets all the .txt files from path'''
    counter = 0
    datafiles = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                counter += 1
                datafiles.append(os.path.join(r, file))
    filenames = list()
    ''''Cuts filename'''
    for f in datafiles:
        filenames.append(f.replace(r"C:\Users\BenE\Desktop\Python\Projects\reddit project\datasets", ''))
#        print(filenames)
    
    count = 0
    for fname in filenames:
        print ('(',count,')',fname)
        count += 1
    
    filenumber = int(input("Select file number:"))
    file = datafiles[filenumber]
    
    fh = open(file)
    
    postinfolist = fh.readlines()
    
    postinfolist = list(postinfolist)
    
#    print(postinfolist)
    for week in postinfolist:
        postinfolist = ast.literal_eval(week)
        
#    for post in postinfolist:
#        print (post,'\n\n\n')
    fh.close   
    return postinfolist

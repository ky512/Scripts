import os
rootdir=os.getcwd()
#print(rootdir)
fr=open("./file.txt","w")
for (dirpath, dirnames, filenames) in os.walk(rootdir):

    fr.writelines(dirpath+">>>"+"\n")
    
    for dirname in dirnames:
        print('dirname = ' + dirname)
    for filename in filenames:   
        fr.writelines(os.path.join(dirpath,filename)+"\n")
        #print(os.path.join(dirpath, filename))
        #if(filename=='path1-1.1.txt'):
            #os.chdir(dirpath)        
           # os.rename('path1-1.1.txt', 'path1-1.1.new.txt')
       # print('fileName = ' + filename)
    fr.writelines("\n")
fr.close()




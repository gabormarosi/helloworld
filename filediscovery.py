import os
def search(path,ext):
    files = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            #print("add dir: "+path+"/"+fname)
            files.extend(search(path+"/"+fname,".py"))
            #print("dir found: "+path+"/"+fname)
        elif fname[-3:] == ext:
            #print("py found: "+fname)
            files.append(path+"/"+fname)
            #print("files: "+files)
    #print(filelist)
    return files
#files = search(os.path.abspath("/"),".py")
files = search(os.path.abspath(os.path.expanduser("~")+"/playground"),".py")
print(files)
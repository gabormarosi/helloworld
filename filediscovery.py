import os
def search(path):
    files = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            #print("add dir: "+path+"/"+fname)
            files.extend(search(path+"/"+fname))
            #print("dir found: "+path+"/"+fname)
        elif fname[-3:] == ".py":
            #print("py found: "+fname)
            files.append(path+"/"+fname)
            #print("files: "+files)
    #print(filelist)
    return files
#files = search(os.path.abspath("/"))
files = search(os.path.abspath("/home/mgabee/playground"))
print(files)
def show_files (obj):
    """This is a function to list all the files and sub folders in a given directory"""
    import os
    items = os.listdir(obj)
    files=[]
    for i in items:
        if os.path.isdir(i):
            path=os.path.join(obj,i)
            files.append(show_files(path))
        else:
            files.append(i)
    return files



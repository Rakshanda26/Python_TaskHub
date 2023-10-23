def find_pdfs (files):
    """This is a function to identify the PDF files in a given directory"""
    pdfs=[]
    for i in files:
        extention=""
        flag=0
        for j in i:
            if j==".":
                flag=1
            if flag==1:
                extention=extention+j
        if extention == ".pdf" and flag==1:
            pdfs.append(i)
    return pdfs
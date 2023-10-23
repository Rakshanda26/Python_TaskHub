def combiner (files,address):
    """This is a function to merge several pdf files in a given list"""
    if len(files)>=1:
        from PyPDF2 import PdfFileMerger, PdfFileReader
        mergedObject = PdfFileMerger()
        for fileNumber in range(len(files)):
            mergedObject.append(PdfFileReader(address+'/'+files[fileNumber], 'rb'))
        mergedObject.write(address+"/MergedFiles.pdf")
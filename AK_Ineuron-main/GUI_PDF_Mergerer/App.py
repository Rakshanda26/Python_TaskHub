from tkinter import *
import list_dir
import pdf_indentifier
import pdf_merger

import logging
logging.basicConfig(filename= "logs.log", level = logging.DEBUG, format ='%(asctime)s %(levelname)s %(message)s')

def PDF_Merger() :
    """This is an App to combine all PDFs in a given directory"""
    
    logging.info("PDF_Merger App is called from main")
    
    main_window=Tk()
    
    logging.info("Declaring labels for GUI")
    Label(main_window, text="-x-x-x-x-x--PDF finder & merger--x-x-x-x-x-").grid(row=0,column=1)
    Label(main_window, text="Enter The directory to be checked:-").grid(row=3,column=0)
    Label(main_window, text="-------------------------------------------").grid(row=17,column=1)
    Label(main_window, text="Output").grid(row=18,column=0)
    
    
    logging.info("Declaring entry boxes for GUI")
    add=Entry(main_window,width=50,borderwidth=5)
    add.grid(row=3,column=2)
    op=Entry(main_window,width=50,borderwidth=5)
    op.grid(row=18,column=2)
    
    def act ():
        logging.info("Action function is called through GUI")
        address=add.get()
        
        files=list_dir.show_files(address)
        logging.info("All files in entered directory are lised")
        
        pdfs= pdf_indentifier.find_pdfs(files)
        logging.info("PDF files from entered directory are identified")
        
        pdf_merger.combiner(pdfs,address)
        
        if len(pdfs)==0:
            s="Entered Directory does not have PDF files"
            op.insert(0,s)
        else:
            s= "Combined PDF is available at:"+address+"/MergedFiles"
            op.insert(0,s)
    
    logging.info("Declaring buttons")
    Button(main_window, text="Find & Merge PDFs",command= act).grid(row=4,column=2)
    
    logging.info("Initiating main loop on GUI")
    main_window.mainloop()
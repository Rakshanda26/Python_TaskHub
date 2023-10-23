import logging
from Words_Finder import get_words

logging.basicConfig(filename= "BOW.log", level = logging.DEBUG, format ='%(asctime)s %(levelname)s %(message)s')


def all_words (*files):
    """This is a function to find all the unique words from multiple files & Loading the data SQLite database"""
    
    logging.info("all_words is called")

    try:
        addresses=[]
        for i in files:
            addresses.append(i)
        logging.info("All addresses are seperated")
    
        words=[]
        for address in addresses:
            temp=get_words(address)
            words.append(temp)
        logging.info("Unique words are identified from each file seperatly")
    
        d={}
        for i in words:
            for j in i:
                d[j]=0
        logging.info("Unique words are identified from all files")
    
        l=[]
        for i in d:
            l.append(str(i))
    
        import sqlite3  
    
        db = sqlite3.connect('SQLiteDB_BOW.db')
        cursor = db.cursor()   
        cursor.execute('CREATE TABLE Words(Word TEXT)')
        logging.info("Database & table created")
    
        for i in l:
            cursor.execute("INSERT INTO Words VALUES (?)",[i])
        db.commit()
        logging.info("Words added in database")
        
        for i in cursor.execute("SELECT * FROM Words"):
            print(i)
     
    except Exception as e:
        return(e)
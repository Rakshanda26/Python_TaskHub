import logging
logging.basicConfig(filename= "BOW.log", level = logging.DEBUG, format ='%(asctime)s %(levelname)s %(message)s')

def get_words (address):
    """This is a function to extract all the english words from the given file"""
    
    try:
        logging.info("get_words function is called to extract words from given file")
    
        f= open(address,"r+",encoding="utf-8")
        logging.info("File at given address is opened in r+ mode with utf-8 coding")
    
        content = f.read()
        logging.info("Data from the file is red successfully")
    
        string_list = content.split("\n")
        logging.info("Each record from file is seperated as an individual string")
    
        word_list=[]
        for i in string_list:
            temp=""
            for j in i:
                if 65<= ord(j) and ord(j)<=122:
                    temp=temp+j
            if len(temp) > 0 :
                word_list.append(temp)
        logging.info("Each individual string is checked and words are extracted from file")
    
        return word_list
    
    except:
        return ("Incorrect Attributes")
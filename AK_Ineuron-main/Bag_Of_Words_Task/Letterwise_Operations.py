import logging
logging.basicConfig(filename= "BOW.log", level = logging.DEBUG, format ='%(asctime)s %(levelname)s %(message)s')

def first_letter_occurances (words):
    """This is a function to count number of first letter occurances from given words list"""
    
    logging.info("first_letter_occurances is called")
    
    try:
        d={}
        s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        l=[]
    
        for i in s:
            d[i]=0
        logging.info("All character's occurances are initialised to zero")

        for i in words:
            try:
                d[i[0]]=d[i[0]]+1
            except:
                pass
        logging.info("All character's occurances counts are updated")

        for i in d:
            temp=(i,d[i])
            l.append(temp)
        logging.info("Occurance values of all characters are added in touple form")
    
        return l
    
    except:
        return("Incorrect attributes are passed")
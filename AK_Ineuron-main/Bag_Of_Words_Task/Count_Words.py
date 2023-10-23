import logging
logging.basicConfig(filename= "BOW.log", level = logging.DEBUG, format ='%(asctime)s %(levelname)s %(message)s')

def count_occurance (words):
    """This is a function to list the occurance of every word in a given file"""
    
    try:
        logging.info("count_occurance function is called")
    
        d={}
        l=[]

        for i in words:
            d[i]=0
        logging.info("Initialized all words in dictonary with count 0")
    
        for i in words:
            d[i]=d[i]+1
        logging.info("Updated the count of every word in file")

        for i in d:
            temp=(i,d[i])
            l.append(temp)
        logging.info("Converted word counts into touples and updated in list")
    
        return l
    
    except:
        return("Incorrect attributes")
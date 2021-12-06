import logging

logging.basicConfig(filename="newfile.log",  format='%(asctime)s -%(levelname)s- %(message)s', datefmt='%d-%b-%y %H:%M:%S' ,
               filemode='w')  
  
#Creating an object of the logging  
logger=logging.getLogger()  
logging.disable('DEBUG')
  
#Setting the threshold of logger to DEBUG  
logger.setLevel(logging.NOTSET)  

def log_info_writer(message):
    logger.info(message)

def log_error_writer(message):
    logger.error(message)

def log_warning_writer(message):
    logger.warning(message)

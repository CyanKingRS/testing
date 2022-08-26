
from datetime import datetime
import os

class CSV_Writer:
    '''Class to write info into a CSV type file.'''
    filename = ""
    file = None
    
    
    def __init__(self, dev):
        self.device = dev
        self.__createfile()
        self.__open_file()
        
        
    def write(self, *info):
        '''Writes info to file'''
        for i in info:
            self.file.write(f"{i};")
        self.file.write('\n')
        
        
    def __createfile(self):
        '''Creates the file.'''
        now = datetime.now()
        try:
            os.makedirs(os.getcwd() +"/results", mode=0o777, exist_ok=False)
            os.chmod(os.getcwd() +"/results",mode=0o777)
        except:
            pass
        dt_string = now.strftime("%Y-%m-%d_%H:%M:%S")
        self.filename = os.getcwd() + "/results/"+ str(self.device) + "-" + str(dt_string) + ".csv"
        
        
    def __open_file(self):
        '''Opens the file for writting.'''
        try:
            self.file = open(self.filename, 'w')
            os.chmod(self.filename, mode=0o777)
        except PermissionError as e:
            print("Cannot create .csv file. Check the program's permisions.")
            raise RuntimeError from e
        
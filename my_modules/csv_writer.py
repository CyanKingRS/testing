
from datetime import datetime
import os

class CSV_Writer:
    
    filename = ""
    file = None
    
    
    def __init__(self, dev):
        self.device = dev
        self.__createfile()
        self.__open_file()
        
        
    def write(self, *info):
        for i in info:
            self.file.write(f"{i};")
        self.file.write('\n')
        
        
    def __createfile(self):
        now = datetime.now()
        try:
            os.makedirs(os.getcwd() +"/results", exist_ok=False)
        except:
            pass
        dt_string = now.strftime("%Y-%m-%d_%H:%M:%S")
        self.filename = os.getcwd() + "/results/"+ str(self.device) + "-" + str(dt_string) + ".csv"
        
        
    def __open_file(self):
        try:
            self.file = open(self.filename, 'w')
        except PermissionError as e:
            print("Cannot create .csv file. Check the program's permisions.")
            raise RuntimeError from e
        


import json
import os


class JSON_handler:

    
    __config = None
    __message = None

    
    def __init__(self, path='config.json'):
        if not self.__load_config(path):
            raise Exception(self.__message)

        
    def __load_config(self, path):
        if not os.path.exists(os.getcwd() + "/" + path):
            self.__message = 'Error: could not find file.'
            return None
        
        try:
            config = open(path, "r")
        except:
            self.__message = "Error: could not open file."
            return None
        
        data = config.read()
        
        try:
            json.loads(data)
        except:
            self.__message = "Error: file data is not JSON."
            return None
        
        self.__config = json.loads(data)
        config.close()
        return True


    def read(self):
        return self.__config
        
    
    
           


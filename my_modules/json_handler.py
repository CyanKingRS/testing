

import json
import os


class JSON_handler:

    
    __config = None
    __message = None

    
    def __init__(self, path='config.json'):
        if not self.__load_config(path):
            raise Exception(self.__message)

        
    def __load_config(self, path):
        if not '/' in path: 
            if not os.path.exists(os.getcwd() + "/" + path):
                self.__message = 'Error: could not find file.'
                return None
        else:
            if not os.path.exists(path):
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
        
    
    def read_type(self, name, ind):
        index = 0
        for i in self.__config["devices"]:
            if name == i['name'] and index == ind:
                return i['type']
            elif index != ind:
                index += 1 
           
    def read_ssh_info(self, dev_number):
        return self.__config['devices'][dev_number]['ssh_name'], self.__config['devices'][dev_number]['ssh_password'], self.__config['devices'][dev_number]['ssh_ip']

    def find_device(self, dev_name:str, num:int):
        """This function finds if the device that is being tested is in the config file and returns it's number in the list."""
        index1 = 0
        index = 0
        for i in self.__config['devices']:
            if dev_name.casefold().__eq__(i['name'].casefold()) and (index1 == num):
                
                return index
            elif index1 != num:
                index1 +=1
            else:
                index += 1
                index1 == 0
                
        return None
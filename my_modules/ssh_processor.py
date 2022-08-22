'''Device command tessting process with serial connection.'''


import os
import serial

from my_modules.info_printer import Printer
from my_modules.json_handler import JSON_handler
from my_modules.at_handler import Handler


class Serial_processor:
    def __init__(self, printer: Printer, handler: Handler, configer:JSON_handler, ser:serial.Serial(), name):
        os.system('ssh root@' + ip)
        self.printer = printer
        self.handler = handler
        self.configer = configer
        
        self.ser = ser
        self.__start(name)


    

    def __start(self, name):
        data = self.configer.read()
        
        dev_number = self.handler.find_device_name(name, data)
        
        self.handler.write_device_info(self.ser)
        
        self.printer.print_device(name)
        
        self.handler.process_all_commands(self.ser, data, dev_number)
        


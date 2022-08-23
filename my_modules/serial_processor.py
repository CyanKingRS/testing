'''Device command tessting process with serial connection.'''


import os

import serial

from my_modules.serial_command_processor import Ser_command_processor
from my_modules.csv_writer import CSV_Writer
from my_modules.info_printer import Printer
from my_modules.json_handler import JSON_handler
from my_modules.serial_at_handler import Serial_AT_handler


class Serial_processor:
    def __init__(self, configer:JSON_handler, name='trm240', port='/dev/ttyUSB2'):
        os.system('systemctl stop ModemManager.service')
        self.printer=Printer()
        
        self.handler=Serial_AT_handler(
            csv_writer=CSV_Writer(name),
            cmd_processor=Ser_command_processor(),
            printer=Printer())
        
        self.configer=configer
        
        self.ser=serial.Serial(
                port=port,
                baudrate=115200,
                bytesize=serial.EIGHTBITS,
                xonxoff = False,
                rtscts = False,
                parity = serial.PARITY_NONE,
                stopbits = serial.STOPBITS_ONE,
                timeout=0.5
        ) 
        self.__start(name)


    

    def __start(self, name):
        data = self.configer.read()
        
        dev_number = self.configer.find_device(name)
        
        self.handler.write_device_info(self.ser)
        
        self.printer.print_device(name)
        
        self.handler.process_all_ser_commands(self.ser, data, dev_number)
        


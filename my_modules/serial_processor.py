'''Device command tessting process with serial connection.'''


import os

import serial

from serial import SerialException
from my_modules.serial_command_processor import Ser_command_processor
from my_modules.csv_writer import CSV_Writer
from my_modules.info_printer import Printer
from my_modules.serial_at_handler import Serial_AT_handler


class Serial_processor:
    '''Class to process serial at command testing.'''
    def __init__(self, configer, args):
        os.system('systemctl stop ModemManager.service')
        self.printer=Printer()
        
        self.handler=Serial_AT_handler(
            csv_writer=CSV_Writer(args.device),
            cmd_processor=Ser_command_processor(),
            printer=Printer())
        
        self.configer=configer
        try:
            self.ser=serial.Serial(
                    port=args.serial_port,
                    baudrate=args.baudrate,
                    bytesize=serial.EIGHTBITS,
                    xonxoff = False,
                    rtscts = False,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    timeout=0.5
            ) 
            self.__start(args.device, args.dev_num)
        except SerialException as se:
            print("Error: No such port file exists: " + args.serial_port)
            raise Exception(se)

    

    def __start(self, name, dev_num):
        
        dev_index = self.configer.find_device(name, dev_num)
        
        self.handler.write_device_info(self.ser)
        
        self.handler.process_all_commands(self.ser, self.configer.read(), dev_index)
        


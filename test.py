
from sys import argv

import serial

from my_modules.at_handler import Handler
from my_modules.command_processor import Command_processor
from my_modules.csv_writer import CSV_Writer
from my_modules.info_printer import Printer
from my_modules.json_handler import JSON_handler
from my_modules.serial_processor import Serial_processor

try:
    script, device = argv
    print("Starting...")
    configer = JSON_handler()
    data = configer.read()
    devlist = data["devices"]
    for i in devlist:
        if device == i['name']:
            connect_type = i['type']
    
    connect_module_name =  connect_type  + "_processor"
    
    module = __import__("my_modules." + connect_module_name, fromlist=[connect_module_name.capitalize()])
    obj = getattr(module, connect_module_name.capitalize())(printer=Printer(), 
                                                            handler=Handler(
                                                                csv_writer=CSV_Writer(device),
                                                                cmd_processor=Command_processor(),
                                                                printer=Printer()), 
                                                            configer=configer,
                                                            ser=serial.Serial(
                                                                    port='/dev/ttyUSB2',
                                                                    baudrate=115200,
                                                                    bytesize=serial.EIGHTBITS,
                                                                    xonxoff = False,
                                                                    rtscts = False,
                                                                    parity = serial.PARITY_NONE,
                                                                    stopbits = serial.STOPBITS_ONE,
                                                                    timeout=0.5
                                                            ), 
                                                            name=device)
    
    # x = Serial_processor(printer=Printer(), 
    #                      handler=Handler(
    #                          csv_writer=CSV_Writer(device),
    #                          cmd_processor=Command_processor(),
    #                          printer=Printer()), 
    #                      configer=configer,
    #                      ser=serial.Serial(
    #                             port='/dev/ttyUSB2',
    #                             baudrate=115200,
    #                             bytesize=serial.EIGHTBITS,
    #                             xonxoff = False,
    #                             rtscts = False,
    #                             parity = serial.PARITY_NONE,
    #                             stopbits = serial.STOPBITS_ONE,
    #                             timeout=0.5
    #                      ), 
    #                      name=device)
    
    
    
    print("Done. The log file can be found in /results folder.")
except ValueError as v:
     print("Erorr: Bad arguments.")
     raise Exception(v)


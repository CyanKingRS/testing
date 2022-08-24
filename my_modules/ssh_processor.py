'''Device command tessting process with serial connection.'''


import time

import paramiko

from my_modules.csv_writer import CSV_Writer
from my_modules.info_printer import Printer
from my_modules.ssh_at_handler import Ssh_AT_handler
from my_modules.ssh_command_processor import Ssh_command_processor


class Ssh_processor:
    def __init__(self,  configer, args):
        self.printer=Printer()
        self.handler=Ssh_AT_handler(
            csv_writer=CSV_Writer(args.device),
            cmd_processor=Ssh_command_processor(),
            printer=Printer()
        )
        self.configer = configer
        self.data = self.configer.read()
        self.dev_number = self.configer.find_device(args.device, args.dev_num)
        self.__login(args.ssh_port, args.ssh_ip, args.ssh_username, args.ssh_password)
        
        self.ssh.exec_command('/etc/init.d/gsmd stop')
        self.shell = self.ssh.invoke_shell()
        
        self.shell.send('socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r')
        time.sleep(0.5)
        i = self.shell.recv(-1)
        
        self.__start(args.device)


    

    def __start(self, name):
        
        self.handler.write_device_info(self.ssh, name)
        
        self.printer.print_device(name)
        
        self.handler.process_all_commands(self.shell, self.data, self.dev_number)
       
        

    def __login(self, port, ip, username, password):
        
        
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, port, username, password)

'''Device command tessting process with serial connection.'''


import paramiko

from my_modules.csv_writer import CSV_Writer
from my_modules.info_printer import Printer
from my_modules.json_handler import JSON_handler


class Ssh_processor:
    def __init__(self,  configer:JSON_handler, name='rutx11', port=22):
        self.printer=Printer()
        
        self.configer = configer
        
        self.__login(name, port)
        
        self.ssh.exec_command('/etc/init.d/gsmd stop')
        
        self.ssh.exec_command('socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r')
        
        
        self.__start(name)


    

    def __start(self, name):

       pass
        

    def __login(self, name, port):
        self.data = self.configer.read()
        self.dev_number = self.configer.find_device(name)
        username, password, ip = self.configer.read_ssh_info(self.dev_number) 
        
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, port, username, password)

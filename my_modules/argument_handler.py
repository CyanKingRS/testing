

import argparse

from my_modules.json_handler import JSON_handler


class Argument_handler:
    '''A class to handle argument understanding and parsing.'''
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-d','--device', dest='device',type=str, required=True, help="Testing device name, that matches the name in the config.")
        self.parser.add_argument('-shp', '--shell_port', dest='ssh_port', type=int, default=22, help='The ssh port of the device. Default: 22 or config')
        self.parser.add_argument('-sp', '--serial_port', dest='serial_port', type=str, default='/dev/ttyUSB2', help='The serial port of the device. Default: /dev/ttyUSB2 or config value.')
        self.parser.add_argument('-dn', '--dev_num', dest='dev_num', type=int, default=0, help='Device number to use if multiple devices of the same name are in the config file. Default: 0')
        self.parser.add_argument('-b', '--broadband', dest='broadband', type=int, default='115200', help='Broadband for serial connections. Default: 115200 or config value.')
        self.parser.add_argument('-ip', dest='ssh_ip', type=str, default='192.168.1.1', help='Specify the ip of the testing device for ssh connection. Default: 192.168.1.1 or config value.')
        self.parser.add_argument('-un', '--username', dest='ssh_username', type=str, default='admin', help='Specify the username for ssh connection. Default: admin or config value.')
        self.parser.add_argument('-pw', '--password', dest='ssh_password', type=str, default='Admin123', help='Specify the password of the user for ssh connection. Default: Admin123 or config value.')
        self.parser.add_argument('-c', '--config', dest='config', type=str, default='config.json', help='Specify the path of the config file. Default: ~/config.json')
        
    def configure_and_get_arguments(self):
        '''Method to get arguments from command line and asign them correctly. The options in config file overwrite the text input if the config option is not empty. 
        If both config and command line are empty the default values are used.'''
        args = self.parser.parse_args()
        
        configer = JSON_handler(args.config)
        
        dev_index = configer.find_device(args.device, args.dev_num)
        data = configer.read()['devices'][dev_index]
        type = configer.read_type(args.device, args.dev_num)
        
        if type == 'ssh':
            if data['port']:
                self.parser.set_defaults(ssh_port=data['port'])
            if data['ssh_name']:
                self.parser.set_defaults(ssh_username=data['ssh_name'])
            if data['ssh_ip']:
                self.parser.set_defaults(ssh_ip=data['ssh_ip'])
            if data['ssh_password']:
                self.parser.set_defaults(ssh_password=data['ssh_password'])
    
        elif type == 'serial':
            if data['port']:
                self.parser.set_defaults(serial_port=data['port'])
            if data['baudrate']:
                self.parser.set_defaults(baudrate=data['baudrate'])
    
        return configer, self.parser.parse_args()
        
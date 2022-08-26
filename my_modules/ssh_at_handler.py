

# from my_modules.csv_writer import CSV_Writer
# from my_modules.info_printer import Printer
# from my_modules.ssh_command_processor import Ssh_command_processor


class Ssh_AT_handler:
    '''A class that handles the at command testing of a ssh connection.'''
    def __init__(self, csv_writer, cmd_processor, printer):
        self.csv_writer = csv_writer
        self.cmd_processor = cmd_processor
        self.printer = printer
        
        
    def process_all_commands(self, shell, data, dev_number, ip):
        '''Method to go through all the config commands, test them and print the results. Throws an error if incorrect config file, or device is not found.'''
        try:
            device = data['devices'][dev_number]
            max_tests = len(device['commands'])
            self.csv_writer.write("Command","Expected","Response","Result")
            
            index = 0
            for j in device['commands']:
                index+=1
                
                self.printer.print_test_info(index, max_tests, j['command'], j['expected'], device['name'])
                
                response, res = self.cmd_processor.check_command(shell, j['command'], j['expected'], ip, j['arguments'] )
                
                self.printer.print_result(response, res)
                if res:
                    self.csv_writer.write(j['command'], j['expected'], response, 'Passed')
                else:
                    self.csv_writer.write(j['command'], j['expected'], response, 'Failed')
                
        except KeyError as k:
            print("Error: incorrect config file.")
            raise Exception(k)
        except TypeError as t:
            print("Error: device not found in config file.")
            raise Exception(t)
    
    
    def write_device_info(self, ssh, device):
        '''Method that gets the device info from shell connection and compares it to the user's given name. If incorrect, throws an exception.'''
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ubus call mnfinfo get_value '{\"key\": \"name\"}'")
        txt = ssh_stdout.readlines()
        name = txt[1].split('"')[-2][0:6]
        if device.casefold() == name.casefold():
            self.csv_writer.write('Modem: ' + name)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("gsmctl -w -m -y")
            txt = ssh_stdout.readlines()
           
            mnf_name = txt[0].strip('\n').rstrip()
            mnf_model = txt[1].strip('\n').rstrip()
            mnf_rev = txt[2].strip('\n').rstrip()
            self.csv_writer.write(mnf_name, mnf_model, 'Revision: ' + mnf_rev)
        else:
            print("Error: device name and the name given do not match.")
            raise Exception
        
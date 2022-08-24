


# from my_modules.csv_writer import CSV_Writer
# from my_modules.info_printer import Printer
# from my_modules.ssh_command_processor import Ssh_command_processor


class Ssh_AT_handler:
    
    def __init__(self, csv_writer, cmd_processor, printer):
        self.csv_writer = csv_writer
        self.cmd_processor = cmd_processor
        self.printer = printer
        
        
    def process_all_commands(self, shell, data, dev_number):
        try:
            device = data['devices'][dev_number]
            
            max_tests = len(device['commands'])
            self.csv_writer.write("Command","Expected","Response","Result")
            
            index = 0
            for j in device['commands']:
                index+=1
                
                self.printer.print_test_info(index, max_tests, j['command'], j['expected'])
                
                response, res = self.cmd_processor.check_command(shell, j['command'], j['expected'], j['arguments'])
                
                self.printer.print_result(response, res)
                
                self.csv_writer.write(j['command'], j['expected'], response, res)
                
        except KeyError as k:
            print("Error: incorrect config file.")
            raise Exception(k)
        except TypeError as t:
            print("Error: device not found in config file.")
            raise Exception(t)
    
    
    def write_device_info(self, ssh, device):
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ubus call mnfinfo get_value '{\"key\": \"name\"}'")
        txt = ssh_stdout.readlines()
        name = txt[1].split('"')[-2][0:6]
        if device.casefold() == name.casefold():
            self.csv_writer.write('Modem: ' + name)
        else:
            print("Error: device name and the name given do not match.")
            raise Exception
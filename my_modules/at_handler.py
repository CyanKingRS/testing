


from my_modules.command_processor import Command_processor
from my_modules.csv_writer import CSV_Writer
from my_modules.info_printer import Printer


class Handler:
    

    def __init__(self, csv_writer:CSV_Writer, cmd_processor:Command_processor, printer:Printer):
        self.csv_writer = csv_writer
        self.cmd_processor = cmd_processor
        self.printer = printer
        

    def process_all_commands(self, ser, data, dev_number):
        """This function checks if the device is in the config file and then tests all the commands."""
        try:
            devices = data['devices']
            device = devices[dev_number]
            max_tests = self.find_test_number(data, dev_number)
            self.csv_writer.write("Command", "Expected","Response","Result")
            
            index = 0
            for j in device['commands']:
                index += 1
                self.printer.print_test_info(index, max_tests, j['command'], j['expected'])
                response, res = self.cmd_processor.check_command(ser, j['command'], j['expected'], j['arguments'])
                self.printer.print_result(response, res)
                self.csv_writer.write(j['command'], j['expected'], response, res)
                
        except KeyError as k:
            print("Error: incorrect config file.")
            raise Exception(k)
        except TypeError as t:
            print("Error: device not found in config file.")
            raise Exception(t)
                


    def find_device_name(self, dev_name, data):
        """This function finds if the device that is being tested is in the config file and returns it's number in the list."""
        index = 0
        for i in data['devices']:
            if dev_name.casefold() == i['name'].casefold():
                return index
            
            else:
                index += 1
                
        return None



    def find_test_number(self, data, dev_number):
        try:
            devices = data['devices']
            device = devices[dev_number]
            return len(device['commands'])
        
        except:
            print("Error: The device is not in the config file.")
            
    
    def write_device_info(self, ser):
        "A function which gets the device info from the connected device and uploads it to the csv file."
        self.cmd_processor.send_command(ser, "ATE1")
        self.cmd_processor.send_command( ser, "AT+GMI")
        resp_man = self.cmd_processor.get_dev_info(ser)
        self.cmd_processor.send_command( ser, "AT+CGMM")
        resp_mod = self.cmd_processor.get_dev_info(ser)
        self.csv_writer.write("Manufacturer: " + resp_man, "Model: " + resp_mod )
        
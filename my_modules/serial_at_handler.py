


class Serial_AT_handler:
    '''A class to handle AT command testing using a serial connection.'''

    def __init__(self, csv_writer, cmd_processor, printer):
        self.csv_writer = csv_writer
        self.cmd_processor = cmd_processor
        self.printer = printer
        

    def process_all_commands(self, ser, data, dev_number):
        """This function checks if the device is in the config file and then tests all the commands."""
        try:
            device = data['devices'][dev_number]
            
            max_tests = len(device['commands'])
            self.csv_writer.write("Command", "Expected","Response","Result")
            
            index = 0
            for j in device['commands']:
                index += 1
                
                self.printer.print_test_info(index, max_tests, j['command'], j['expected'], device['name'])
                
                response, res = self.cmd_processor.check_command(ser, j['command'], j['expected'], j['arguments'])
                
                self.printer.print_result(response, res)
                
                self.csv_writer.write(j['command'], j['expected'], response, res)
                
        except KeyError as k:
            print("Error: incorrect config file.")
            raise Exception(k)
        except TypeError as t:
            print("Error: device not found in config file.")
            raise Exception(t)
                

            
    
    def write_device_info(self, ser):
        "A function which gets the device info from the connected device and uploads it to the csv file."
        response, res = self.cmd_processor.check_command(ser, "ATE1", 'OK')
        if res:
            resp_man = self.cmd_processor.get_dev_info(ser, "AT+GMI")
            resp_mod = self.cmd_processor.get_dev_info(ser, "AT+CGMM")
            self.csv_writer.write("Manufacturer: " + resp_man, "Model: " + resp_mod )
        
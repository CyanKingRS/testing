from operator import truediv
import time


class Ser_command_processor:
    '''A class that has methods to test device's commands using a serial connection'''

    def __init__(self):
        pass
    
    
    def check_command(self, ser, command, expected, args=None):
        """A method used to check the given command's output by comparring to the expected one. Returns a boolean and the response."""
        ser_cpy = ser
        for i in range(5):
            try:
                if ser == None:
                    ser = ser_cpy
                    ser.open()
                self.send_command( ser, command)
                if args:
                    for i in args:
                        self.send_command(ser, i)
                    
                response = self.get_response(ser)    
                return response, response==expected
            except OSError as ose:
                ser.close()
                ser = None
                time.sleep(8)
                print("Error: connection lost. Retrying...")
        print("Error: no connected device.")
        raise Exception()
        
        
        
    def get_response(self, ser):
        """A method used to get the response of AT command. Returns a response as a string"""
        txt = self.__read_until_resp(ser)
        try:
            split_txt = txt.split(b"\n")
            resp_str = split_txt[-2].decode('utf-8').rstrip()
        except IndexError as ie:
            print("Error: Unknown command or too little wait time.")
            resp_str = "timeout".rstrip()
            raise Exception(ie)
        return resp_str


    def send_command(self, ser, command, timeout=0.5):
        '''Method that send the command to serial device and waits for the set timeout.'''
        ser.write(command.encode() + b"\r")
        time.sleep(timeout)


    def get_dev_info(self, ser, cmd):
        '''Method to get device info.'''
        ser_cpy = ser
        while True:
            try:
                if ser == None:
                    ser = ser_cpy
                    ser.open()
                self.send_command( ser, cmd)
                txt = self.__read_until_resp(ser)
                split_txt = txt.split(b'\n')
                info_str = split_txt[1].decode('utf-8').rstrip()
                return info_str
            except OSError as ose:
                ser.close()
                ser = None
                time.sleep(8)
                print("Error: connection lost. Retrying...")
        
        


    def __read_until_resp(self, ser):
        '''Method to wait and get response from the device. Returns the response or "timeout"'''
        timeout = time.time() + 180
        txt=''
        while time.time() < timeout:
                txt = ser.read()           
                time.sleep(1)              
                data_left = ser.inWaiting()
                txt += ser.read(data_left)
                if txt:
                    return txt
           
        return 'timeout'
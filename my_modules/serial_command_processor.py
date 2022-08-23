import time


class Ser_command_processor:


    def __init__(self):
        pass
    
    
    def check_command(self, ser, command, expected, args=None):
        """A method used to check the given command's output by comparring to the expected one. Returns a boolean."""
        self.send_command( ser, command)
        if args:
            for i in args:
                self.send_command(ser, i)
            
        response = self.get_response(ser)    
        return response, response==expected
        
        
        
    def get_response(self, ser):
        """A method used to get the response of AT command. Returns a response as a string"""
        txt = ser.readall()
        split_txt = txt.split(b"\n")
        try:
            resp_str = split_txt[-2].decode('utf-8').rstrip()
        except IndexError as ie:
            print("Error: Unknown command or too little wait time.")
            resp_str = "timeout".rstrip()
        return resp_str


    def send_command(self, ser, command, timeout=0.5):
        ser.write(command.encode() + b"\r")
        time.sleep(timeout)


    def get_dev_info(self, ser):
        txt = ser.readall()
        split_txt = txt.split(b'\n')
        info_str = split_txt[1].decode('utf-8').rstrip()
        return info_str

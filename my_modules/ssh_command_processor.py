
import time


class Ssh_command_processor:
    
    def __init__(self):
        pass
    
    
    
    def check_command(self, shell, command, expected, args=None):
        self.send_command(shell, command)
        if args:
            for i in args:
                self.send_command(shell, i)
                
        response = self.get_response(shell)
        return response, response==expected
    
    
    def send_command(self, shell, command, timeout=0.6):
        shell.send(command+'\r')
        time.sleep(timeout)
        
    def get_response(self, shell):
        txt = shell.recv(-1)
        split_txt = txt.split(b'\n\n\n')
        print(split_txt)
        try:
            resp_str = split_txt[-1].decode('utf-8').strip('\n')
        except IndexError as ie:
            print("Error: Unknown command or too little wait time.")
            resp_str = "timeout".rstrip()
        return resp_str
        
    def get_dev_info(self, shell):
        txt = shell.recv(-1)
        split_txt = txt.split(b'\n\n\n')
        info_str = split_txt[1].decode('utf-8').strip('\n')
        return info_str
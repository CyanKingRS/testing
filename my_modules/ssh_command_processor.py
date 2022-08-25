
import subprocess
import time


class Ssh_command_processor:
    '''Class that is used to process the at commands when testing with a ssh connection.'''
    def __init__(self):
        pass
    
    
    
    def check_command(self, shell, command, expected, ip, args=None):
        '''Checks if the command given returns the correct result and returns the response and if the command passed.'''
        for i in range(5):
            try:
                self.check_ping(ip)
                self.send_command(shell, command)
                if args:
                    for i in args:
                        self.check_ping(ip)
                        self.send_command(shell, i)
                        
                self.check_ping(ip)        
                response = self.get_response(shell)
                
                return response, response==expected
            except subprocess.CalledProcessError:
                time.sleep(8)
                print("Error: connection lost. Retrying...")
                
            
    
    
    def send_command(self, shell, command, timeout=0.5):
        '''Sends the command to the shell and waits fot the set time.'''
        shell.send(command+'\r')
        time.sleep(timeout)
        
        
        
    def get_response(self, shell):
        '''Receives the response and returns it. If the function takes too long returns timeout.'''
        timeout = time.time() + 180
        is_timeout = True
        txt = b''
        
        while time.time() < timeout:
            buf = shell.recv(-1)
            if (not buf) and (b'\n\n\n' in txt):
               is_timeout = False
               break
            txt += buf
        
        if not is_timeout:
            try:
                split_txt = txt.split(b'\n\n\n')
                resp_str = split_txt[-1].decode('utf-8').strip('\n')
            except IndexError as ie:
                print("Error: Cannot get split text. Command reading incorrect.")
                resp_str = "timeout".rstrip()
        else:
            resp_str = "timeout"
        return resp_str
        



    def check_ping(self, ip_address):
        '''Method to ping the device.'''
        subprocess.check_call(
            ['ping', '-c', '1', ip_address],
            stdout=subprocess.DEVNULL,  
            stderr=subprocess.DEVNULL
        )

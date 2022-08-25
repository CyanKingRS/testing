
import os
import time
from colorama import init
from termcolor import colored


class Printer:
    """Class that acts as a printer to the computer's terminal."""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        init()
    
    
    def print_device(self, dev):
        """A method prints the device name to the command line."""
        print(colored("Current testing device: " + dev, 'cyan'))
        
        
    def print_test_info(self, index, max_index, cmd, exp_res, device):
        """A method that prints test information to the command line."""
        self.clear_text()
        self.print_device(device)
        print(f"Current test: {index} / {max_index}. Command: {cmd}. Expected result: {exp_res}.\nWaiting for response...")
        
        
    def print_result(self, response, res):
        """A method that prints the results of the test to the command line."""
        if res:
            print(f"Response: {response}. Result: " + colored("Passed.", 'green'))
            self.passed += 1
        else:
            print(f"Response: {response}. Result: " + colored("Failed.", 'red'))
            self.failed += 1

        print(colored(f"Passed tests: {self.passed}.", 'green') +colored(f"Failed tests: {self.failed}.", 'red')+"\n")
       
        
    def clear_text(self):
        '''Clears the screen for other test text.'''
        time.sleep(1.5)
        os.system('clear')




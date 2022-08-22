from colorama import init
from termcolor import colored


class Printer:
    
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        init()
    
    
    def print_device(self, dev):
        print(colored("Current testing device:" + dev, 'cyan'))
        
        
    def print_test_info(self, index, max_index, cmd, exp_res):
        print(f"Current test: {index} / {max_index}. Command: {cmd}. Expected result: {exp_res}.\n Waiting for response...")
        
        
    def print_result(self, response, res):
        if res:
            print(f"Response: {response}. Result: " + colored("Passed.", 'green'))
            self.passed += 1
        else:
            print(f"Response: {response}. Result: " + colored("Failed.", 'red'))
            self.failed += 1

        print(colored(f"Passed tests: {self.passed}.", 'green') +colored(f"Failed tests: {self.failed}.", 'red')+"\n")





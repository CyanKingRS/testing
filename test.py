
from sys import argv, stdout
import time
import paramiko
from my_modules.json_handler import JSON_handler


def main(script, *args:list[str]):
    try:
        
        print("Starting" + script +"...")
        
        configer = JSON_handler()
        if args:
            connect_type = configer.read_type(args[0])
        
        connect_module_name =  connect_type  + "_processor"
        
        module = __import__("my_modules." + connect_module_name, fromlist=[connect_module_name.capitalize()])
        obj = getattr(module, connect_module_name.capitalize())(configer, *args)

        print("Done. The log file can be found in /results folder.")
    except ValueError as v:
        print("Erorr: Bad arguments.")
        raise Exception(v)



main(*argv)

# ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.1.1', 22, "root",'Admin123')
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('/etc/init.d/gsmd stop')
        
# shell = ssh.invoke_shell()
# time.sleep(0.5)
# shell.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r")
# time.sleep(0.5)
# shell.send('ATE1\r')
# shell.send('ATE1\r')
# shell.send('ATE1\r')
# shell.send('ATE1\r')
# shell.send('ATE1\r')
# shell.send('ATE1\r')
# time.sleep(0.5)
# shell.send("ls -l\r")
# print(shell.recv(-1))


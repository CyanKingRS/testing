# Automatic AT Command Testing Script
This project was made to test AT commands (also known as Hayes commands) on ruoters with a SSH or Serial connection from linux os computers. 


## Starting
To start the tests download all the files, configure the config file to have the correct information (look bellow for example), then open the terminal and run the script with administration privelages. 
Example: sudo python3 test.py -d <testing_device_name>

The possible arguments that can be passed launching the command are:
-  -h, --help                                    Show help message and exit
-  -d DEVICE, --device DEVICE                    Testing device name, that matches the name in the config. Must be passed otherwise the program won't start.
-  -shp SSH_PORT, --shell_port SSH_PORT          The ssh port of the device. Default: 22 or config
-  -sp SERIAL_PORT, --serial_port SERIAL_PORT    The serial port of the device. Default: /dev/ttyUSB2 or config value.
-  -dn DEV_NUM, --dev_num DEV_NUM                Device index to use if multiple devices of the same name are in the config file. Default: 0
-  -b BROADBAND, --broadband BROADBAND           Broadband for serial connections. Default: 115200 or config value.
-  -ip SSH_IP                                    Specify the ip of the testing device for ssh connection. Default: 192.168.1.1 or config value.
-  -un SSH_USERNAME, --username SSH_USERNAME     Specify the username for ssh connection. Default: admin or config value.
-  -pw SSH_PASSWORD, --password SSH_PASSWORD     Specify the password of the user for ssh connection. Default: Admin123 or config value.
-  -c CONFIG, --config CONFIG                    Specify the path of the config file. Default: ~/config.json

Passed arguments will only change the default values of the nesecery options. Config options override the arguments. Therefore, most of the configuration should be done in the config file. Basically, if config options are empty, then arguments will be taken, if no arguments are given, general default values are used.

## Config examples
The config.json file is a JSON file. Therefore, all rules that would apply a regular JSON file still apply. These variables can be changed:
- "name" can be changed to any desired string. However, if the argument is incorrect when lauching the script an error will occur, because the "name" string needs to match the argument passed. The uppercase and lowercase charecters do not differ from each other when comparing. 
- "type" can be either serial or ssh depending on which connection type the router uses.
- "commands". Commands to test can be added to this list. The command structure is {"command":"full_command","expected":"expected_result", "arguments":"additional_strings_sent_after_command"}. The arguments can be either a list or empty.


For serial connection these options are necesery to be included:
- "port" can be changed to the usb port of the testing device. Can be found in /dev/ folder on linux.
- "baudrate" can be changed to the baudrate required for comunication with the device.

For ssh connection these options are necesery:
- "port" can be changed to the ssh port of the device. 
- "ssh_name" can be changed to the username of the ssh connection.
- "ssh_ip" can be changed to the ip address of the conneted device.
- "ssh_password" can be changed to the password of the ssh connection.

Example:
{
    "devices":[
        {
            "name":"trm240",
            "type":"serial",
            "port":"/dev/ttyUSB2",
            "baudrate":"115200",
            "commands":[
                {"command":"ATE1","expected":"OK", "arguments":""},
                {"command":"AT+CMGF=1","expected":"OK", "arguments":""},
                {"command":"AT+CMGS=?","expected":"OK", "arguments":[]},
            ]
        },
        {
            "name":"rutx11",
            "type":"ssh",
            "port":"22",
            "ssh_name":"root",
            "ssh_ip":"192.168.1.1",
            "ssh_password":"Admin123",
            "commands":[
                {"command":"AT","expected":"OK","arguments":""},
                {"command":"ATE1","expected":"OK","arguments":""},
                {"command":"AT+CMGF=1","expected":"OK","arguments":""},
                {"command":"AT+CMGS=?","expected":"OK","arguments":[]}
            ]
        }
    ]
}

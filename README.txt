#Automatic AT Command Testing Script
This project was made to test AT commands (also known as Hayes commands) on ruoters with a SSH or Serial connection from linux os computers. 


##Starting
To start the tests download all the files, configure the config file to have the correct information (look bellow for example), then open the terminal and run the script with administration privelages. 
Example: sudo python3 test.py <testing_device_name>

##Config examples
The config.json file is a JSON file. Therefore, all rules that would apply a regular JSON file still apply. These variables can be changed:
- "name" can be changed to any desired string. However, if the argument is incorrect when lauching the script an error will occur, because the "name" string needs to match the argument passed. The uppercase and lowercase charecters do not differ from each other when comparing. 
- "commands". Commands to test can be added to this list. The command structure is {"command":"full_command","expected":"expected_result", "arguments":"additional_strings_sent_after_command"}. The arguments can be either a list or empty.
Example:
{
    "devices":[
        {
            "name":"trm240","commands":[
                {"command":"ATE1","expected":"OK", "arguments":""},
                {"command":"AT+CMGF=1","expected":"OK", "arguments":""},
                {"command":"AT+CMGS=\"+37063834583\"","expected":"OK", "arguments":["Test.","\u001a"]}
            ]
            "name":"RutX11","commands":[
                {"command":"ATE1","expected":"OK", "arguments":""},
                {"command":"AT+CMGF=1","expected":"OK", "arguments":""},
                {"command":"AT+CMGS=\"+37063834583\"","expected":"OK", "arguments":["Test.","\u001a"]}
            ]
            
        }
    ]
}


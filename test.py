
from sys import argv


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



from my_modules.argument_handler import Argument_handler



def main():
    try:
        print("Starting...")
        arg_parser = Argument_handler()
        configer, args = arg_parser.configure_and_get_arguments()
        if args:
            connect_type = configer.read_type(args.device, args.dev_num)
        
        connect_module_name =  connect_type  + "_processor"
        
        module = __import__("my_modules." + connect_module_name, fromlist=[connect_module_name.capitalize()])
        obj = getattr(module, connect_module_name.capitalize())(configer, args)

        print("Done. The log file can be found in /results folder.")
    except ValueError as v:
        print("Erorr: Bad arguments.")
        raise Exception(v)


    
    
    
main()

import sys
import os, fnmatch
import subprocess
    

def print_type(subcommand, path):
    
    if subcommand == 'exit':
        print(subcommand, "is a shell builtin")
    elif subcommand == 'echo':
        print(subcommand, "is a shell builtin")
    elif subcommand == 'type':
        print(subcommand, "is a shell builtin")
    else:
        for x in path:
            text = x + "/" + subcommand
            if os.path.isfile(text):
                return print(subcommand, "is", text)
        sys.stdout.write(f"{subcommand}: not found\n")

def check_program(program, path):
    for x in path:
        text = x + "/" + program.lower().split()[0]
        if os.path.isfile(text):
            return True
    return False

def run_program(program, path):
    for x in path:
        text = x + "/" + program.lower().split()[0]
        if os.path.isfile(text):
            os.system(text + " " + program.split()[1])
            return 0
    return 0

def print_exit():
    sys.exit(0)

def print_echo(subcommand):
    print(subcommand)

def main():
    # Wait for user input
    while True:
        PATH = os.environ['PATH'].split(":")
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        

        if command.lower().split()[0] == 'type':
            print_type(command[command.index(" ")+1:], PATH)
        elif command.lower().split()[0] == 'exit':
            print_exit()
        elif command.lower().split()[0] == 'echo':
            print_echo(command[command.index(" ")+1:])
        elif check_program(command, PATH):
            run_program(command, PATH)
        else:
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()




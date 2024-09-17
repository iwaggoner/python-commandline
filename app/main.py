import sys
import os, fnmatch
    

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
        else:
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()



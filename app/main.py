import sys


def main():
    
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()

        if command.split()[0] == 'exit':
            sys.exit(0)
        if command.split()[0] == 'echo':
            print(command[command.index(" ")+1:])
        else:
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()

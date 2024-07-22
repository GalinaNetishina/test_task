from source import *


if __name__ == "__main__":
    while True:
        task, *args = input().replace(')', '').split('(')
        print(lm.execute_command(task, ''.join(args)))


from library_manager import librarian as lm


if __name__ == "__main__":
    while True:
        task, *args = input().replace(')', '').split('(')
        lm.execute_command(task, ''.join(args))


        # match task:
        #     case task if task.startswith('add'):
        #         com, args = task.split('(')
        #         id = lm.commands[com](*[arg.strip(' )') for arg in args.split(',')])
        #     case com, path if com in ['save', 'load']:
        #         try:
        #             lm.commands[com](path)
        #         except:
        #             print('error')
        #     case com if com in ['load', 'save']:
        #         lm.commands[com]()
        #     case com if com == 'show':
        #         lm.commands[com]()
        #     case task if task.startswith('delete'):
        #         com, args = task.split('(')
        #         id = lm.commands[com](args.strip(' )'))
        #     case _:
        #         print('unknown task')
        #         show_menu()

from source import *

menu = {
    'show': {
        'func': lm.show_all,
        'description': 'Вывести все книги',
        'parameters': ''},
    'load': {
        'func': lm.load_library,
        'description': 'Загрузить книги из storage/library.json',
        'parameters': ''},
    'save': {
        'func': lm.save_library,
        'description': 'Сохранить книги в storage/library.json',
        'parameters': ''},
    'add': {'args': 'args',
            'func': lm.add_book,
            'description': 'Добавить книгу с указанием названия, автора, года',
            'parameters': '(title, author, year)'},
    'del': {
        'args': 'single',
        'func': lm.delete_book,
        'description': ' Удалить книгу, если существует',
        'parameters': '(id:четыре цифры)'},
    'set': {
        'args': 'args',
        'func': lm.change_status,
        'description': ' Изменить статус',
        'parameters': '(id:четыре цифры, status: 0="В наличии"/1="Выдана")'},
    'search': {
        'args': 'kwargs',
        'func': lm.search,
        'description': 'Выводит таблицу с результатами поиска',
        'parameters': '(key=value) Допустимые значения для key: year/title/author))'},
    'sort': {
        'args': 'kwargs',
        'func': lm.sort_by,
        'description': 'Выводит таблицу, отсортированную по ключу',
        'parameters': '(key=(одно из полей year/title/author/status))'
    }
        }


def show_menu():
    for command, info in menu.items():
        print(f'{command}{info["parameters"]} - {info["description"]}')


def execute(command, args_string=None):
    """execute command from user's input, convert args to required format for command"""
    if args_string is None:
        return menu[command]['func']()
    match menu[command]['args']:
        case 'args':
            args = args_string.split(', ')
            return menu[command]['func'](*args)
        case 'single':
            return menu[command]['func'](args_string)
        case 'kwargs':
            if command == 'sort':
                res = menu[command]['func'](key=args_string)
            else:
                pairs = args_string.split(', ')
                args = {}
                for item in pairs:
                    key, value = item.split('=')
                    args[key] = value
                res = menu[command]['func'](**args)
            for i in res:
                print(i)


if __name__ == "__main__":
    show_menu()
    while True:
        try:
            task, *args = input('Введите команду:\n').replace(')', '').split('(')
            if args:
                execute(task, args[0])
            else:
                execute(task)

        except Exception as e:
            print(e)
            show_menu()

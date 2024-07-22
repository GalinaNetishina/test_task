import json

from source.Book import Book


class Librarian:
    books = {}

    def __init__(self):
        self.show_menu()

    @classmethod
    def show_menu(cls):
        commands = {'add': cls.add_book,
                    'delete': cls.delete_book,
                    'save': cls.save_library,
                    'load': cls.load_library,
                    'show': cls.show_all,
                    'change_status': cls.change_status,
                    'search': cls.search,
                    }
        print('Введите команду:\n' +
              '\n'.join([f"  {command + str(function.__doc__)}" for command, function in commands.items()]))

    @classmethod
    def execute_command(cls, command: str, args: str):
        """Выполняет введенную команду (из списка доступных) с переданными в виде строки аргументами,  разделенными запятой"""
        commands = {'add': cls.add_book,
                    'delete': cls.delete_book,
                    'save': cls.save_library,
                    'load': cls.load_library,
                    'show': cls.show_all,
                    'change_status': cls.change_status,
                    'search': cls.search,
                    }
        try:
            if command == 'search':
                res = commands[command](args)
            if command in commands:
                if args:
                    res = commands[command](*args.split(', '))
                else:
                    res = commands[command]()
            else:
                print('Uncorrect command')
                cls.show_menu()
        except ValueError as e:
            print(e)
        else:
            return res

    @classmethod
    def add_book(cls, title: str, author: str, year: int):
        """(Название, Автор, Год издания) - Добавить книгу"""
        try:
            new_book = Book(title, author, year)
            cls.books[new_book.id] = new_book
            return new_book.id
        except ValueError as e:
            print(e)

    @classmethod
    def delete_book(cls,   id: int):
        """(id) - Удалить книгу по id"""
        try:
            return cls.books.pop(id)
        except KeyError:
            print('Ошибка удаления - Такой книги нет')

    @classmethod
    def change_status(cls, id: int, new_status: bool):
        """(id, статус) - Изменить статус книги(0-"Выдана", 1-"В наличии")"""
        if int(new_status) in [0, 1]:
            if cls.books[id].is_available != new_status:
                cls.books[id].toggle_status()
        else:
            raise ValueError('Некорректный статус')
        return 'status changed'

    @classmethod
    def save_library(cls):
        """ - Сохранить книги в json файл"""
        with open('storage/library.json', 'w', encoding='utf8') as f:
            json.dump([book.todict() for book in cls.books.values()], f, ensure_ascii=False, indent=4)
        return 'saved success'

    @classmethod
    def load_library(cls):
        """ - Загрузить книги из json файла"""
        with open('storage/library.json', 'r', encoding='utf8') as f:
            res = json.load(f)
            for book in res:
                id, title, author, year, status = book.values()
                if id in Book._ids:
                    continue
                id = cls.add_book(title, author, year)
                cls.change_status(id, 0 if status == "Выдана" else 1)
        return 'loaded success'

    @classmethod
    def show_all(cls):
        ''' - Вывести таблицу со всеми книгами'''
        print('\n   id   |          title           |       author       |  year  |  status')
        for _, book in cls.books.items():
            print(f'{book.id:^8}|{book.title:^26}|{book.author:^20}|{book.year:^8}|{book.get_status()}')
        return f'Всего: {len(cls.books)} книг'

    @classmethod
    def search(cls, /, **kwargs):
        """(key=value) - поиск книг, где key(title/author/year) = value"""

        res = filter(lambda x: all([x[param] == value for param, value in kwargs.items()]), cls.books.values())
        return res or 'Not found'


librarian = Librarian()


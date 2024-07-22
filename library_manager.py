import json
import sys

from Book import Book


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
                    }
        print('Введите команду:\n' +
              '\n'.join([f"  {command + str(function.__doc__)}" for command, function in commands.items()]))

    @classmethod
    def execute_command(cls, command, args):
        commands = {'add': cls.add_book,
                    'delete': cls.delete_book,
                    'save': cls.save_library,
                    'load': cls.load_library,
                    'show': cls.show_all,
                    'change_status': cls.change_status,
                    }
        try:
            if command in commands:
                if args:
                    commands[command](*args.split(', '))
                else:
                    commands[command]()
            else:
                print('Uncorrect command')
                cls.show_menu()
        except ValueError as e:
            print(e)

    @classmethod
    def add_book(cls, title, author, year):
        '''(Название, Автор, Год издания) - Добавить книгу'''
        try:
            new_book = Book(title, author, year)
            cls.books[new_book.id] = new_book
            return new_book.id
        except ValueError as e:
            print(e)

    @classmethod
    def delete_book(cls,   id):
        '''(id) - Удалить книгу по id'''
        try:
            cls.books.pop(id)
        except KeyError:
            print('Ошибка удаления - Такой книги нет')

    @classmethod
    def change_status(cls, id, new_status):
        '''(id, статус) - Изменить статус книги(0-"Выдана", 1-"В наличии")'''
        if new_status in [0, 1]:
            if cls.books[id].is_available != new_status:
                cls.books[id].toggle_status()
            else:
                raise ValueError('Новый статус совпадает с текущим')
        else:
            raise ValueError('Некорректный статус')

    @classmethod
    def save_library(cls):
        ''' - Сохранить книги в json файл'''
        with open('storage/library.json', 'w', encoding='utf8') as f:
            json.dump([book.todict() for book in cls.books.values()], f, ensure_ascii=False, indent=4)

    @classmethod
    def load_library(cls):
        ''' - Загрузить книги из json файла'''
        with open('storage/library.json', 'r', encoding='utf8') as f:
            res = json.load(f)
            for book in res:
                id, title, author, year, status = book.values()
                if id in Book._ids:
                    continue
                id = cls.add_book(title, author, year)
                cls.change_status(id, status)


    @classmethod
    def show_all(cls):
        ''' - Вывести таблицу со всеми книгами'''
        print('\n   id   |          title           |       author       |  year  |  status')
        for _, book in cls.books.items():
            print(f'{book.id:^8}|{book.title:^26}|{book.author:^20}|{book.year:^8}|{book.get_status()}')
        print(f'Всего: {len(cls.books)} книг')
            #time.sleep(0.5)


librarian = Librarian()


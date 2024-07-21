import json

from Book import Book


class Librarian:
    books = dict()

    @staticmethod
    def add_book(title, author, year):
        new_book = Book(title, author, year)
        Librarian.books[new_book.id] = new_book

    @staticmethod
    def delete_book(id):
        try:
            Librarian.books.pop(id)
        except KeyError:
            print('Ошибка удаления - Такой книги нет')

    @staticmethod
    def change_status(id, new_status):
        if new_status in ['В наличии', 'Выдана']:
            if Librarian.books[id].get_status() != new_status:
                Librarian.books[id].toggle_status()
        else:
            print(f'Некорректный статус - {new_status}')

    @staticmethod
    def save_library():
        with open('library.json', 'w', encoding='utf8') as f:
            json.dump([book.todict() for book in Librarian.books.values()], f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_library():
        with open('library.json', 'r', encoding='utf8') as f:
            res = json.load(f)
            for book in res:
                id, title, author, year, status = book.values()
                Librarian.add_book(title, author, year)
                Librarian.change_status(id, status)

    @staticmethod
    def show_all():
        print('\n   id   |          title           |       author       |  status')
        for _, book in Librarian.books.items():
            print(f'{book.id:^8}|{book.title:^26}|{book.author:^20}|{book.get_status()}')
import itertools
import json


from source.Book import Book


class Librarian:
    """class for library managing.
    Library represents by dictionary, with keys - id, and values - instances of class Books"""
    library = {}

    @classmethod
    def add_book(cls, title: str, author: str, year: str):
        """Adds book in class library, requires title, author and correct year, returns id"""
        try:
            new_book = Book(title, author, year)
            cls.library[new_book.id] = new_book
            return new_book.id
        except ValueError as e:
            raise Exception(f'Adding failed - {str(e)}')

    @classmethod
    def delete_book(cls,   id: str):
        """deletes book with id, if it exists in class library"""
        try:
            return cls.library.pop(id)
        except KeyError:
            raise Exception(f'Deleting failed - Book with id {id} is not exist in {cls.library.keys()}')

    @classmethod
    def change_status(cls, id: str, new_status: str):
        """changes status book with id, indicate 0('Выдана) or 1('В наличии')"""
        if int(new_status) in [0, 1]:
            if cls.library[id].is_available != new_status:
                cls.library[id].toggle_status()
        else:
            raise ValueError('Некорректный статус')

    @classmethod
    def save_library(cls):
        """Saves class library as storage/library.json"""
        with open('storage/library.json', 'w', encoding='utf8') as f:
            json.dump([book.todict() for book in cls.library.values()], f, ensure_ascii=False, indent=4)
        return 'saved success'

    @classmethod
    def load_library(cls):
        """Loads class library from storage/library.json"""
        # TODO fix duplication
        with open('storage/library.json', 'r', encoding='utf8') as f:
            for book in json.load(f):
                _, title, author, year, status = book.values()
                id = cls.add_book(title, author, year)
                cls.change_status(id, 0 if status == "Выдана" else 1)
        return 'loaded success'

    @staticmethod
    def _get_books(books, count: int = None):
        """takes iterable object, return generator with sorted list."""
        if count is None:
            yield from (i for i in sorted(books))
        # TODO may indicate, how much elements to get
        else:
            yield from (itertools.islice(sorted(books), count))

    @classmethod
    def show_all(cls):
        """Print table with all books, and total count"""
        print('\n   id   |          title           |       author       |  year  |  status')
        for book in cls._get_books(cls.library.values()):
            print(book)
        print(f'Total: {len(cls.library)} books')

    @classmethod
    def search(cls, **kwargs):
        """Takes pairs key=values arguments, returns generator with founded books.
        Available keys - title, author, year."""
        if 'year' in kwargs:
            kwargs['year']=int(kwargs['year'])
        if any(x not in ['title', 'author', 'year'] for x in kwargs.keys()):
            raise KeyError(f'Invalid key')
        res = filter(lambda x: all(x[key] == value for key, value in kwargs.items()), cls.library.values())
        yield from res

    @classmethod
    def sort_by(cls, key: str):
        """takes key(book's property), returns generator with sorted books"""
        if key not in Book.__slots__:
            raise Exception('Invalid key')
        res = (sorted(cls.library.values(), key=lambda x: x[key]))
        yield from res




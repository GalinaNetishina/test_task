import datetime
import uuid


class Book:
    _ids = set()

    def get_status(self):
        '''return status in text format'''
        return 'В наличии' if self.is_available else 'Выдана'

    @staticmethod
    def is_valid_year(year: int):
        return 1800 < year <= datetime.date.today().year

    @classmethod
    def generate_id(cls):
        '''generate 4-digit uid'''
        while True:
            id = int(uuid.uuid4()) % 10000
            if id not in cls._ids:
                cls._ids.add(str(id).zfill(4))
                yield str(id).zfill(4)

    def __init__(self, title: str, author: str, year: int):
        self.id = next(Book.generate_id())
        self.title = title
        self.author = author
        if Book.is_valid_year(int(year)):
            self.year = year
        else:
            raise ValueError('wrong year')
        self.is_available = 1

    def toggle_status(self):
        '''switch status'''
        self.is_available = not self.is_available

    def todict(self):
        return dict(id=self.id, title=self.title, author=self.author, year=self.year, status=self.get_status())

    def __str__(self):
        return f'Title: {self.title} Author: {self.author} Year:{self.year} Status:{self.get_status()}'

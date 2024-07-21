import json


class Book:
    _id = 0

    def get_status(self):
        return 'В наличии' if self.is_available else 'Выдана'

    def __init__(self, title, author, year):
        Book._id += 1
        self.id = Book._id
        self.title = title
        self.author = author
        self.year = year
        self.is_available = 1

    def toggle_status(self):
        self.is_available = not self.is_available

    def todict(self):
        return dict(id=self.id, title=self.title, author=self.author, year=self.year, status=self.get_status())

    def __str__(self):
        return f'Title: {self.title} Author: {self.author} Year:{self.year} Status:{self.get_status()}'

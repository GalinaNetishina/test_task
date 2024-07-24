import datetime
import uuid


class Book:
    """class represents book

    Attributes:
        title(str), author(str), year(int) - required for initialization, year must be correct
        id(int) unique, generated automatically
        is_available - status in int(boolean) format, default set to 1

    """
    _ids = set()
    __slots__ = ['id', 'title', 'author', 'year', 'is_available', 'status']

    def __init__(self, title: str, author: str, year: int):
        self.id = next(Book.generate_id())
        self.title = title
        self.author = author
        if Book.is_valid_year(int(year)):
            self.year = year
        else:
            raise ValueError('invalid year')
        self.is_available = 1
        self.status = self.get_status()

    # for default sorting
    def __lt__(self, other):
        return ((self.title, self.author, self.year, -self.is_available) <
                (other.title, other.author, other.year, -other.is_available))

    # for subscriptable book
    def __getitem__(self, item):
        return self.todict()[item]

    def get_status(self):
        """return status in text format"""
        return 'В наличии' if self.is_available else 'Выдана'

    @staticmethod
    def is_valid_year(year: int):
        """validate year, not too long ago and not future"""
        return 1800 < year <= datetime.date.today().year

    @classmethod
    def generate_id(cls):
        """generate 4-digit uid"""
        while True:
            id = int(uuid.uuid4()) % 10000
            if id not in cls._ids:
                cls._ids.add(str(id).zfill(4))
                yield str(id).zfill(4)

    def toggle_status(self):
        """switch status"""
        self.is_available = not self.is_available
        self.status = self.get_status()

    def todict(self):
        return dict(id=self.id, title=self.title, author=self.author, year=self.year, status=self.status)

    def __str__(self):
        return f'{self.id:^8}|{self.title:^26}|{self.author:^20}|{self.year:^8}|{self.status}'
        # return f'Book #{self.id} - {",".join([str(k) + ": " + str(v) for k, v in self.todict().items()])}'

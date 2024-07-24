import unittest
from source import *


class TestBookInnerMethod(unittest.TestCase):
    def test_year_is_valid(self):
        self.assertTrue(Book.is_valid_year(2024))
        self.assertTrue(Book.is_valid_year(2000))
        self.assertTrue(Book.is_valid_year(1910))

    def test_year_isnot_valid(self):
        self.assertFalse(Book.is_valid_year(2025))
        self.assertFalse(Book.is_valid_year(1000))
        self.assertFalse(Book.is_valid_year(3000))

    def test_generate_uuid(self):
        test_uuids = {next(Book.generate_id()) for _ in range(100)}
        self.assertSetEqual(test_uuids, Book._ids)


class TestBookClass(unittest.TestCase):
    def init_correct(self):
        test_books = ['book1, author1, 2020', 'book2, author2, 2021', 'book3, author2, 2022']
        for book_data in test_books:
            self.assertDictEqual(Book(*book_data.split(', ')).todict(), {'title': book_data[0], 'author': book_data[1], 'year': book_data[2]})


if __name__ == '__main__':
    unittest.main()

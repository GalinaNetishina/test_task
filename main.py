from Book import Book
from library_manager import Librarian

Librarian.load_library()
Librarian.add_book('book4', 'author1', 1995)
Librarian.add_book('book5', 'author1', 1990)
Librarian.add_book('book6', 'author3', 1980)
Librarian.show_all()

Librarian.change_status(1, 'Выдана')
#
Librarian.save_library()
Librarian.show_all()
Librarian.change_status(3, "В наличии")

from library import Book, User


class LibraryKeywords:
    def create_user(self, name):
        return User(name)

    def create_book(self, title, author, pages, isbn):
        return Book(title, author, pages, isbn)

    def reserve_book(self, user, book):
        user.reserve_book(book)

    def take_book(self, user, book):
        user.take_book(book)

    def return_book(self, user, book):
        User.return_book(book, user)

    def is_book_reserved(self, book):
        return book.is_reserved

    def is_book_taken(self, book):
        return book.current_user is not None

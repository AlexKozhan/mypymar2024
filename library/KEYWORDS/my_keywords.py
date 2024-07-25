"""
This module contains test functions
for interacting with Book and User
objects from the library_1 module.
"""

from library_1 import Book, User


def test_reserve_book():
    """
    Test reserving a book by a user.

    Returns:
        str: A message indicating the
        result of the reservation.
    """
    book = Book("Test Book", "Author",
                100, "12345")
    user = User("User1")
    return user.reserve_book(book)


def test_take_book():
    """
    Test taking a book by a user.

    Returns:
        str: A message indicating the result of
        taking the book.
    """
    book = Book("Test Book",
                "Author", 100, "12345")
    user = User("User1")
    return user.take_book(book)


def test_return_book():
    """
    Test returning a book by a user.

    Returns:
        str: A message indicating the result
        of returning the book.
    """
    book = Book("Test Book",
                "Author", 100, "12345")
    user = User("User1")
    user.take_book(book)
    return user.return_book(book)


def test_take_reserved_book_by_another_user():
    """
    Test another user attempting to take
    a book that is already reserved.

    Returns:
        str: A message indicating the result
        of the attempt to take the reserved book.
    """
    book = Book("Test Book", "Author",
                100, "12345")
    user1 = User("User1")
    user2 = User("User2")
    user1.reserve_book(book)
    return user2.take_book(book)

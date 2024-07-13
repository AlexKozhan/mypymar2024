"""
This module defines the Book and User
classes for a simple library system.
It includes methods to reserve, take, and
return books, as well as basic logging for actions performed.
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        pages (int): The number of pages in the book.
        isbn (str): The ISBN number of the book.
        is_reserved (bool): Indicates whether
        the book is reserved.
        current_user (User): The user who
        currently has the book.
    """

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False
        self.current_user = None

    def reserve(self, user):
        """
        Reserve the book for a user.

        Args:
            user (User): The user who wants
            to reserve the book.

        Returns:
            bool: True if the reservation
            was successful, False otherwise.
        """
        logger.info("Attempting to reserve "
                    "book '%s' by user %s.", self.title, user.name)
        if self.is_reserved:
            logger.info("Book '%s' is "
                        "already reserved by "
                        "user %s.", self.title, self.current_user.name)
            return False
        self.is_reserved = True
        self.current_user = user
        logger.info("Book '%s' is reserved "
                    "by user %s.", self.title, user.name)
        return True

    def take(self, user):
        """
        Take the book for a user.

        Args:
            user (User): The user who
            wants to take the book.

        Returns:
            bool: True if the book was
            successfully taken, False otherwise.
        """
        logger.info("Attempting to take book '%s' "
                    "by user %s.", self.title, user.name)
        if self.current_user is not None and self.current_user != user:
            logger.info("Book '%s' is already "
                        "taken by user %s.", self.title, self.current_user.name)
            return False
        self.current_user = user
        self.is_reserved = False
        logger.info("Book '%s' is taken "
                    "by user %s.", self.title, user.name)
        return True

    def return_book(self, user):
        """
        Return the book by a user.

        Args:
            user (User): The user who wants to return the book.

        Returns:
            bool: True if the book was successfully
            returned, False otherwise.
        """
        logger.info("Attempting to return "
                    "book '%s' by user %s.", self.title, user.name)
        if self.current_user is None:
            logger.info("Book '%s' is "
                        "not taken by anyone.", self.title)
            return False
        logger.info("Book '%s' is returned "
                    "by user %s.", self.title, self.current_user.name)
        self.current_user = None
        self.is_reserved = False
        return True


class User:
    """
    Represents a user in the library system.

    Attributes:
        name (str): The name of the user.
    """
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        """
        Reserve a book for the user.

        Args:
            book (Book): The book to be reserved.

        Returns:
            bool: True if the reservation
            was successful, False otherwise.
        """
        return book.reserve(self)

    def take_book(self, book):
        """
        Take a book for the user.

        Args:
            book (Book): The book to be taken.

        Returns:
            bool: True if the book was
            successfully taken, False otherwise.
        """
        return book.take(self)

    @staticmethod
    def return_book(book, user):
        """
        Return a book by the user.

        Args:
            book (Book): The book to be returned.
            user (User): The user who is returning the book.

        Returns:
            bool: True if the book was
            successfully returned, False otherwise.
        """
        return book.return_book(user)

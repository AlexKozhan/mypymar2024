"""
This module defines the Book and User classes for a simple library system.
It includes methods to reserve, take, and return books, as well as basic logging for actions performed.
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
        is_reserved (bool): Indicates whether the book is reserved.
        current_user (User): The user who currently has the book.
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
            bool: True if the reservation was
            successful, False otherwise.
        """
        logger.info(f"Attempting to reserve "
                    f"book '{self.title}' by user {user.name}.")
        if self.is_reserved:
            logger.info(f"Book '{self.title}' is "
                        f"already reserved by "
                        f"user {self.current_user.name}.")
            return False
        else:
            self.is_reserved = True
            self.current_user = user
            logger.info(f"Book '{self.title}' is "
                        f"reserved by user {user.name}.")
            return True

    def take(self, user):
        """
        Take the book for a user.

        Args:
            user (User): The user who wants
            to take the book.

        Returns:
            bool: True if the book was successfully
            taken, False otherwise.
        """
        logger.info(f"Attempting to take book '{self.title}' "
                    f"by user {user.name}.")
        if (self.current_user is not None
                and self.current_user != user):
            logger.info(f"Book '{self.title}' is "
                        f"already taken by "
                        f"user {self.current_user.name}.")
            return False
        elif self.is_reserved and self.current_user != user:
            logger.info(f"Book '{self.title}' is already "
                        f"reserved by "
                        f"user {self.current_user.name}.")
            return False
        else:
            self.current_user = user
            self.is_reserved = False
            logger.info(f"Book '{self.title}' is "
                        f"taken by user {user.name}.")
            return True

    def return_book(self, user):
        """
        Return the book by a user.

        Args:
            user (User): The user who wants to
            return the book.

        Returns:
            bool: True if the book was successfully
            returned, False otherwise.
        """
        logger.info(f"Attempting to return book '{self.title}' "
                    f"by user {user.name}.")
        if self.current_user is None:
            logger.info(f"Book '{self.title}' is "
                        f"not taken by anyone.")
            return False
        elif self.current_user != user:
            logger.info(f"Book '{self.title}' cannot "
                        f"be returned by user {user.name} "
                        f"because it is taken "
                        f"by {self.current_user.name}.")
            return False
        else:
            logger.info(f"Book '{self.title}' is "
                        f"returned by "
                        f"user {self.current_user.name}.")
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
            bool: True if the reservation was
            successful, False otherwise.
        """
        return book.reserve(self)

    def take_book(self, book):
        """
        Take a book for the user.

        Args:
            book (Book): The book to be taken.

        Returns:
            bool: True if the book was successfully
            taken, False otherwise.
        """
        return book.take(self)

    @staticmethod
    def return_book(book, user):
        """
        Return a book by the user.

        Args:
            book (Book): The book to be returned.
            user (User): The user who is
            returning the book.

        Returns:
            bool: True if the book was
            successfully returned, False otherwise.
        """
        return book.return_book(user)

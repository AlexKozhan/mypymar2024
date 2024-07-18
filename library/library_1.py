"""
This module defines two classes: Book and User,
representing a basic
book management system where users can reserve,
take, and return books.
"""


class Book:
    """
    Represents a book with attributes like title,
    author, pages, and ISBN.
    Users can reserve, take, and return books
    through methods provided.
    """
    def __init__(self, title, author, pages, isbn):
        """
        Initialize a Book object with its title,
        author, pages, and ISBN.
        Initially, the book is not reserved and
        has no current user.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False
        self.current_user = None

    def reserve(self, user):
        """
        Reserve the book for a specific user.

        Args:
            user (User): The user who wants to
            reserve the book.

        Returns:
            str: A message indicating the success or
            failure of the reservation.
        """
        if self.is_reserved:
            return (f"Book '{self.title}' is already "
                    f"reserved by user {self.current_user.name}.")

        self.is_reserved = True
        self.current_user = user
        return (f"Book '{self.title}' is "
                f"reserved by user {user.name}.")

    def take(self, user):
        """
        Allow a user to take the book if it's not
        reserved or reserved by them.

        Args:
            user (User): The user who wants to
            take the book.

        Returns:
            str: A message indicating the success
            or failure of taking the book.
        """
        if self.is_reserved and self.current_user != user:
            return (f"Book '{self.title}' is already "
                    f"reserved by user {self.current_user.name}.")

        if self.current_user is not None:
            return (f"Book '{self.title}' is already "
                    f"taken by user {self.current_user.name}.")

        self.current_user = user
        self.is_reserved = False
        return f"Book '{self.title}' is taken by user {user.name}."

    def return_book(self, user):
        """
        Allow a user to return the book if they
        have it checked out.

        Args:
            user (User): The user who wants to
            return the book.

        Returns:
            str: A message indicating the success or
            failure of returning the book.
        """
        if self.current_user is None:
            return (f"Book '{self.title}' is not taken "
                    f"by anyone.")

        if self.current_user != user:
            return (f"Book '{self.title}' cannot be returned "
                    f"by user {user.name} because it is "
                    f"taken by {self.current_user.name}.")

        self.current_user = None
        self.is_reserved = False
        return (f"Book '{self.title}' is returned "
                f"by user {user.name}.")


class User:
    """
    Represents a user with a name who can interact
    with books by reserving, taking, and returning them.
    """
    def __init__(self, name):
        """
        Initialize a User object with a given name.

        Args:
            name (str): The name of the user.
        """
        self.name = name

    def reserve_book(self, book):
        """
        Reserve a specified book for the user.

        Args:
            book (Book): The book to reserve.

        Returns:
            str: A message indicating the success
            or failure of the reservation.
        """
        return book.reserve(self)

    def take_book(self, book):
        """
        Take a specified book if available or
        reserved by the user.

        Args:
            book (Book): The book to take.

        Returns:
            str: A message indicating the success
            or failure of taking the book.
        """
        return book.take(self)

    def return_book(self, book):
        """
        Return a book that the user has borrowed.

        Args:
            book (Book): The book to return.

        Returns:
            str: A message indicating the success
            or failure of returning the book.
        """
        return book.return_book(self)

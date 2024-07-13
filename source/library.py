import logging

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Book:
    """
    Class representing a book in the library.
    """

    def __init__(self, title, author, pages, isbn):
        """
        Initialize a book object.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            pages (int): Number of pages in the book.
            isbn (str): ISBN of the book.
        """
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
            user (User): User object who wants to reserve the book.

        Returns:
            bool: True if the book is successfully
            reserved, False otherwise.
        """
        logger.info("Attempting to reserve "
                    "book '%s' by "
                    "user %s.", self.title, user.name)
        if self.is_reserved:
            logger.info("Book '%s' is already "
                        "reserved by user %s.",
                        self.title, self.current_user.name)
            return False
        self.is_reserved = True
        self.current_user = user
        logger.info("Book '%s' is reserved "
                    "by user %s.", self.title, user.name)
        return True

    def take(self, user):
        """
        Take the book by a user.

        Args:
            user (User): User object who wants
            to take the book.

        Returns:
            bool: True if the book is successfully
            taken, False otherwise.
        """
        logger.info("Attempting to take "
                    "book '%s' by user %s.",
                    self.title, user.name)
        if (self.current_user is not None
                and self.current_user != user):
            logger.info("Book '%s' is already"
                        " taken by user %s.",
                        self.title, self.current_user.name)
            return False
        if self.is_reserved and self.current_user != user:
            logger.info("Book '%s' is "
                        "already reserved by user %s.",
                        self.title, self.current_user.name)
            return False
        self.current_user = user
        self.is_reserved = False
        logger.info("Book '%s' is taken by user %s.",
                    self.title, user.name)
        return True

    def return_book(self, user):
        """
        Return the book by a user.

        Args:
            user (User): User object who wants to
            return the book.

        Returns:
            bool: True if the book is successfully
            returned, False otherwise.
        """
        logger.info("Attempting to return book '%s' "
                    "by user %s.", self.title, user.name)
        if self.current_user is None:
            logger.info("Book '%s' is not taken "
                        "by anyone.", self.title)
            return False
        if self.current_user != user:
            logger.info("Book '%s' cannot be returned "
                        "by user %s because it is taken "
                        "by %s.", self.title,
                        user.name, self.current_user.name)
            return False
        logger.info("Book '%s' is returned by "
                    "user %s.", self.title,
                    self.current_user.name)
        self.current_user = None
        self.is_reserved = False
        return True


class User:
    """
    Class representing a user of the library.
    """

    def __init__(self, name):
        """
        Initialize a user object.

        Args:
            name (str): Name of the user.
        """
        self.name = name

    def reserve_book(self, book):
        """
        Reserve a book.

        Args:
            book (Book): Book object to be reserved.

        Returns:
            bool: True if the book is successfully
            reserved, False otherwise.
        """
        return book.reserve(self)

    def take_book(self, book):
        """
        Take a book.

        Args:
            book (Book): Book object to be taken.

        Returns:
            bool: True if the book is successfully
            taken, False otherwise.
        """
        return book.take(self)

    @staticmethod
    def return_book(book, user):
        """
        Return a book.

        Args:
            book (Book): Book object to be returned.
            user (User): User object returning the book.

        Returns:
            bool: True if the book is successfully
            returned, False otherwise.
        """
        return book.return_book(user)

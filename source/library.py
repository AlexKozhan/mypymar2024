import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Book:
    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False
        self.current_user = None

    def reserve(self, user):
        logger.info(f"Attempting to reserve book '{self.title}' by user {user.name}.")
        if self.is_reserved:
            logger.info(f"Book '{self.title}' is already reserved by user {self.current_user.name}.")
            return False
        else:
            self.is_reserved = True
            self.current_user = user
            logger.info(f"Book '{self.title}' is reserved by user {user.name}.")
            return True

    def take(self, user):
        logger.info(f"Attempting to take book '{self.title}' by user {user.name}.")
        if self.current_user is not None and self.current_user != user:
            logger.info(f"Book '{self.title}' is already taken by user {self.current_user.name}.")
            return False
        elif self.is_reserved and self.current_user != user:
            logger.info(f"Book '{self.title}' is already reserved by user {self.current_user.name}.")
            return False
        else:
            self.current_user = user
            self.is_reserved = False
            logger.info(f"Book '{self.title}' is taken by user {user.name}.")
            return True

    def return_book(self, user):
        logger.info(f"Attempting to return book '{self.title}' by user {user.name}.")
        if self.current_user is None:
            logger.info(f"Book '{self.title}' is not taken by anyone.")
            return False
        elif self.current_user != user:
            logger.info(f"Book '{self.title}' cannot be returned by user {user.name} "
                        f"because it is taken by {self.current_user.name}.")
            return False
        else:
            logger.info(f"Book '{self.title}' is returned by user {self.current_user.name}.")
            self.current_user = None
            self.is_reserved = False
            return True


class User:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        return book.reserve(self)

    def take_book(self, book):
        return book.take(self)

    @staticmethod
    def return_book(book, user):
        return book.return_book(user)

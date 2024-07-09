class Book:
    """
    Represents a book in the library.
    """

    def __init__(self, title, author, pages, isbn):
        """
        Initialize a Book object.

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
            user (User): User object who wants
            to reserve the book.
        """
        print(f"Attempting to reserve book '{self.title}' "
              f"by user {user.name}.")
        if self.is_reserved:
            print(f"Book '{self.title}' is already reserved "
                  f"by user {self.current_user.name}.")
        else:
            self.is_reserved = True
            self.current_user = user
            print(f"Book '{self.title}' is reserved "
                  f"by user {user.name}.")

    def take(self, user):
        """
        Take the book by a user.

        Args:
            user (User): User object who wants
            to take the book.
        """
        print(f"Attempting to take book '{self.title}' "
              f"by user {user.name}.")
        if (self.current_user is not None and
                self.current_user != user):
            print(f"Book '{self.title}' is already taken "
                  f"by user {self.current_user.name}.")
        elif self.is_reserved and self.current_user != user:
            print(f"Book '{self.title}' is already reserved "
                  f"by user {self.current_user.name}.")
        else:
            self.current_user = user
            self.is_reserved = False
            print(f"Book '{self.title}' is taken "
                  f"by user {user.name}.")

    def return_book(self, user):
        """
        Return the book by a user.

        Args:
            user (User): User object who wants
            to return the book.
        """
        print(f"Attempting to return book '{self.title}' "
              f"by user {user.name}.")
        if self.current_user is None:
            print(f"Book '{self.title}' is not "
                  f"taken by anyone.")
        elif self.current_user != user:
            print(f"Book '{self.title}' cannot "
                  f"be returned by user {user.name} "
                  f"because it is taken by {self.current_user.name}.")
        else:
            print(f"Book '{self.title}' is "
                  f"returned by user {self.current_user.name}.")
            self.current_user = None
            self.is_reserved = False


class User:
    """
    Represents a user of the library.
    """

    def __init__(self, name):
        """
        Initialize a User object with a name.

        Args:
            name (str): Name of the user.
        """
        self.name = name

    def reserve_book(self, book):
        """
        Reserve a book from the library.

        Args:
            book (Book): Book object to be reserved.
        """
        book.reserve(self)

    def take_book(self, book):
        """
        Take a book from the library.

        Args:
            book (Book): Book object to be taken.
        """
        book.take(self)

    @staticmethod
    def return_book(book, user):
        """
        Return a book to the library.

        Args:
            book (Book): Book object to be returned.
            user (User): User object returning the book.
        """
        book.return_book(user)


# Example usage:
book1 = Book("White Fang", "Jack London",
             100, "1234567890")
book2 = Book("Animals", "Ivan Ivanov",
             101, "2232442")

user1 = User("Alex")
user2 = User("Siarhei")

user1.reserve_book(book1)
user2.reserve_book(book2)

user2.take_book(book1)
user1.take_book(book2)

User.return_book(book1, user1)
User.return_book(book2, user2)
User.return_book(book1, user2)

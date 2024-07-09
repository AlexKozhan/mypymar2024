import unittest
from library_1 import Book, User


class TestLibrary(unittest.TestCase):
    """
    Test cases for the Book and User classes.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.book1 = Book("White Fang",
                          "Jack London", 100,
                          "1234567890")
        self.book2 = Book("Animals",
                          "Ivan Ivanov", 101,
                          "2232442")
        self.user1 = User("Alex")
        self.user2 = User("Siarhei")

    def test_reserve_book(self):
        """
        Test the reservation functionality of a book.
        """
        print("\nRunning test_reserve_book")
        self.user1.reserve_book(self.book1)
        print(f"Book1 after reserving by "
              f"user1: {vars(self.book1)}")
        self.assertTrue(self.book1.is_reserved)
        self.assertEqual(self.book1.current_user, self.user1)

        initial_user = self.book1.current_user
        self.user2.reserve_book(self.book1)
        print(f"Book1 after attempting to reserve "
              f"by user2: {vars(self.book1)}")
        self.assertTrue(self.book1.is_reserved)
        self.assertEqual(self.book1.current_user, initial_user)

    def test_take_book(self):
        """
        Test the book borrowing functionality.
        """
        print("\nRunning test_take_book")
        print(f"Initial state of book1: {vars(self.book1)}")

        self.user1.reserve_book(self.book1)
        print(f"After reserving book1 "
              f"by user1: {vars(self.book1)}")

        self.user1.take_book(self.book1)
        print(f"After taking book1 "
              f"by user1: {vars(self.book1)}")

        self.assertEqual(self.book1.current_user, self.user1)
        self.assertFalse(self.book1.is_reserved)

        print(f"Initial state of book2: {vars(self.book2)}")

        self.user2.reserve_book(self.book2)
        print(f"After reserving book2 "
              f"by user2: {vars(self.book2)}")

        initial_user = self.book2.current_user
        self.user1.take_book(self.book2)
        print(f"After attempting to take book2 "
              f"by user1: {vars(self.book2)}")

        self.assertEqual(self.book2.current_user, initial_user)
        self.assertTrue(self.book2.is_reserved)

    def test_return_book(self):
        """
        Test the book return functionality.
        """
        print("\nRunning test_return_book")
        self.user1.take_book(self.book1)
        print(f"After taking book1 by user1: {vars(self.book1)}")
        User.return_book(self.book1, self.user1)
        print(f"After returning book1 "
              f"by user1: {vars(self.book1)}")
        self.assertIsNone(self.book1.current_user)
        self.assertFalse(self.book1.is_reserved)

        User.return_book(self.book2, self.user1)
        print(f"After attempting to return book2 "
              f"by user1: {vars(self.book2)}")
        self.assertIsNone(self.book2.current_user)
        self.assertFalse(self.book2.is_reserved)

        self.user1.take_book(self.book1)
        print(f"After taking book1 again "
              f"by user1: {vars(self.book1)}")
        User.return_book(self.book1, self.user2)
        print(f"After attempting to return book1 "
              f"by user2: {vars(self.book1)}")
        self.assertEqual(self.book1.current_user, self.user1)
        self.assertFalse(self.book1.is_reserved)


if __name__ == '__main__':
    unittest.main(verbosity=2)

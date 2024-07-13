"""
This module contains tests for the library
system including the Book and User classes.
It uses pytest for testing and logging to
capture log messages.
"""

import logging
import pytest
from library import Book, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def setup_library():
    """
    Fixture to set up the library with books
    and users for testing.

    Returns:
        tuple: Contains two book objects and
        two user objects.
    """
    book1 = Book("White Fang", "Jack London",
                 100, "1234567890")
    book2 = Book("Animals", "Ivan Ivanov",
                 101, "2232442")
    user1 = User("Alex")
    user2 = User("Siarhei")
    return book1, book2, user1, user2


def test_reserve_book(setup_library, caplog):
    """
    Test reserving a book.

    Args:
        setup_library (fixture): Fixture
        to set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, _ = setup_library
    with caplog.at_level(logging.INFO):
        assert user1.reserve_book(book1) is True
    assert book1.is_reserved is True
    assert book1.current_user == user1


def test_reserve_already_reserved_book(setup_library, caplog):
    """
    Test reserving a book that is already reserved.

    Args:
        setup_library (fixture): Fixture to
        set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, user2 = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user2.reserve_book(book1) is False
    assert (f"Book '{book1.title}' is already "
            f"reserved by user {user1.name}.") in caplog.text


def test_reserve_book_multiple_times(setup_library, caplog):
    """
    Test a user reserving a book multiple times.

    Args:
        setup_library (fixture): Fixture to set
        up the library.
        caplog (LogCaptureFixture): Fixture to
        capture log messages.
    """
    book1, _, user1, _ = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user1.reserve_book(book1) is False
    assert (f"Book '{book1.title}' is already "
            f"reserved by "
            f"user {user1.name}.") in caplog.text


def test_take_book(setup_library, caplog):
    """
    Test taking a reserved book by another user.

    Args:
        setup_library (fixture): Fixture to
        set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, user2 = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user2.take_book(book1) is False
    assert book1.current_user == user1
    assert book1.is_reserved is True


def test_take_reserved_book(setup_library, caplog):
    """
    Test taking a reserved book by the user
    who reserved it.

    Args:
        setup_library (fixture): Fixture to
        set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, _ = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user1.take_book(book1) is True
    assert (f"Book '{book1.title}' is taken "
            f"by user {user1.name}.") in caplog.text


def test_take_unreserved_book(setup_library, caplog):
    """
    Test taking an unreserved book.

    Args:
        setup_library (fixture): Fixture to
        set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, _, user2 = setup_library
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user2.take_book(book1) is True
    assert (f"Book '{book1.title}' is taken "
            f"by user {user2.name}.") in caplog.text


def test_return_book(setup_library, caplog):
    """
    Test returning a taken book.

    Args:
        setup_library (fixture): Fixture to
        set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, _ = setup_library
    user1.reserve_book(book1)
    user1.take_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert User.return_book(book1, user1) is True
    assert book1.current_user is None
    assert (f"Book '{book1.title}' is returned "
            f"by user {user1.name}.") in caplog.text


def test_return_book_by_another_user(setup_library, caplog):
    """
    Test returning a book by another user.

    Args:
        setup_library (fixture): Fixture to
        set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, user2 = setup_library
    user1.reserve_book(book1)

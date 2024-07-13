"""
This module contains tests for the
library system including the Book and User classes.
It uses pytest for testing and logging
to capture log messages.
"""

import logging
import pytest
from library import Book, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def setup_library():
    """
    Fixture to set up the library with
    books and users for testing.

    Returns:
        tuple: Contains two book objects
        and two user objects.
    """
    book1 = Book("White Fang",
                 "Jack London", 100, "1234567890")
    book2 = Book("Animals",
                 "Ivan Ivanov", 101, "2232442")
    user1 = User("Alex")
    user2 = User("Siarhei")
    return book1, book2, user1, user2


def test_reserve_book(setup_library, caplog):
    """
    Test reserving a book.

    Args:
        setup_library (fixture): Fixture to
        set up the library.
        caplog (LogCaptureFixture): Fixture to
        capture log messages.
    """
    book1, _, user1, _ = setup_library
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user1.reserve_book(book1) is True
    assert (f"Attempting to reserve book "
            f"'White Fang' by user Alex.") in caplog.text
    assert (f"Book 'White Fang' is "
            f"reserved by user Alex.") in caplog.text


def test_take_book(setup_library, caplog):
    """
    Test taking a book.

    Args:
        setup_library (fixture): Fixture
        to set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, _ = setup_library
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user1.take_book(book1) is True
    assert (f"Attempting to take book "
            f"'White Fang' by user Alex.") in caplog.text
    assert (f"Book 'White Fang' is "
            f"taken by user Alex.") in caplog.text


def test_return_book(setup_library, caplog):
    """
    Test returning a book.

    Args:
        setup_library (fixture): Fixture
        to set up the library.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    book1, _, user1, _ = setup_library
    user1.reserve_book(book1)
    user1.take_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert User.return_book(book1, user1) is True
    assert (f"Attempting to return book "
            f"'White Fang' by user Alex.") in caplog.text
    assert (f"Book 'White Fang' is "
            f"returned by user Alex.") in caplog.text

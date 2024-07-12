import pytest
import logging
from library import Book, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def setup_library():
    book1 = Book("White Fang", "Jack London", 100, "1234567890")
    book2 = Book("Animals", "Ivan Ivanov", 101, "2232442")
    user1 = User("Alex")
    user2 = User("Siarhei")
    return book1, book2, user1, user2


def test_reserve_book(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    with caplog.at_level(logging.INFO):
        assert user1.reserve_book(book1) is True
    assert book1.is_reserved is True
    assert book1.current_user == user1


def test_reserve_already_reserved_book(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user2.reserve_book(book1) is False
    assert f"Book '{book1.title}' is already reserved by user {user1.name}." in caplog.text


def test_reserve_book_multiple_times(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user1.reserve_book(book1) is False
    assert f"Book '{book1.title}' is already reserved by user {user1.name}." in caplog.text


def test_take_book(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user2.take_book(book1) is False  # User2 cannot take reserved book
    assert book1.current_user == user1
    assert book1.is_reserved is True


def test_take_reserved_book(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    user1.reserve_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user1.take_book(book1) is True
    assert f"Book '{book1.title}' is taken by user {user1.name}." in caplog.text


def test_take_unreserved_book(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert user2.take_book(book1) is True
    assert f"Book '{book1.title}' is taken by user {user2.name}." in caplog.text


def test_return_book(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    user1.reserve_book(book1)
    user1.take_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert User.return_book(book1, user1) is True
    assert book1.current_user is None
    assert f"Book '{book1.title}' is returned by user {user1.name}." in caplog.text


def test_return_book_by_another_user(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    user1.reserve_book(book1)
    user1.take_book(book1)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        returned_successfully = User.return_book(book1, user2)
    assert returned_successfully is False
    assert (f"Book '{book1.title}' cannot be returned by user {user2.name} "
            f"because it is taken by {user1.name}.") in caplog.text


def test_return_book_not_taken(setup_library, caplog):
    book1, book2, user1, user2 = setup_library
    caplog.clear()
    with caplog.at_level(logging.INFO):
        assert User.return_book(book1, user1) is False
    assert f"Book '{book1.title}' is not taken by anyone." in caplog.text


from app import greet


def test_greet():
    assert greet("Vishal") == "Hello, Vishal! Welcome to CI/CD."


def test_greet_empty_name():
    assert greet("") == "Hello, ! Welcome to CI/CD."

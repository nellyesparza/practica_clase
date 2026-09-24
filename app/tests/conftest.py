# app/tests/conftest.py
import pytest


class RepositorioFalso:
    # Your mock implementation here
    pass


@pytest.fixture
def repo_falso():
    return RepositorioFalso()

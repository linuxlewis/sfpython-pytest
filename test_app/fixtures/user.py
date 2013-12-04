import pytest

from app.model.user import User

from app.factory.user import UserFactory

@pytest.fixture
def user():

    u = User()
    u.id = 2
    u.name = 'Bob'

    UserFactory.USERS.append(u.__dict__)

    return u



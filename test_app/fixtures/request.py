
from pyramid.testing import DummyRequest

import pytest

@pytest.fixture
def request():
    return DummyRequest()


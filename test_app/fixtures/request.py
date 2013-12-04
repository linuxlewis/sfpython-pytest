
import pytest

@pytest.fixture
def request():
    return DummyRequest()

class DummyRequest(object):

    def __init__(self):
        self.params = dict()





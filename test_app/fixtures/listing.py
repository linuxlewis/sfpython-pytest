import pytest

from app.model.listing import Listing

from app.factory.listing import ListingFactory

@pytest.fixture
def listing():
    l = Listing()
    l.id = 2
    l.description = 'hi'
    l.address = '123 fake ave'
    l.price = 1010
    l.expired = False
    l.photos = []

    ListingFactory.LISTINGS.append(l.__dict__)

    return l

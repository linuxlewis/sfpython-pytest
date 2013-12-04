import pytest

from app.model.interaction import Interaction

from app.factory.interaction import InteractionFactory

@pytest.fixture
def interaction(user, listing):
    i = Interaction()
    i.id = 2
    i.user_id = user.id
    i.listing_id = listing.id

    InteractionFactory.INTERACTIONS.append(i.__dict__)

    return i

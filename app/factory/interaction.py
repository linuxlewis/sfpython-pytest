from app.model.interaction import Interaction

class InteractionFactory(object):

    INTERACTIONS = [{'id':1, 'listing_id':1, 'user_id':1, 'events':[]}]

    @staticmethod
    def get_by_id(id):

        return [Interaction.hydrate(x) for x in InteractionFactory.INTERACTIONS if x['id'] == id]
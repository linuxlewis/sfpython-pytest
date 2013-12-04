
class Interaction(object):

    def __init__(self):
        self.events = []
        self.id = None
        self.listing_id = None
        self.user_id = None

    def __repr__(self):
        return 'Interaction(%s)' % str(self.id)

    @classmethod
    def hydrate(cls, x):
        interaction = cls()
        interaction.id = x['id']
        interaction.listing_id = x['listing_id']
        interaction.user_id = x['user_id']
        return interaction


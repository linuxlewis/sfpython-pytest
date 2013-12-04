
class Listing(object):

    def __init__(self):
        self.address = None
        self.description = None
        self.expired = False
        self.id = None
        self.price = None
        self.photos = []

    def __repr__(self):
        return 'Listing(%s)' % str(self.id)

    @classmethod
    def hydrate(cls, x):
        listing = cls()
        listing.address = x['address']
        listing.description = x['description']
        listing.expired = x['expired']
        listing.id = x['id']
        listing.price = x['price']
        listing.photos = x['photos']
        return listing
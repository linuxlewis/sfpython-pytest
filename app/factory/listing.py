from app.model.listing import Listing

class ListingFactory(object):

    LISTINGS = [{'id':1, 'description':'hey', 'address':'123 fake st', 'price':1000, 'expired':False, 'photos':[]}]

    @staticmethod
    def get_by_id(id):

        return [Listing.hydrate(x) for x in ListingFactory.LISTINGS if x['id'] == id]




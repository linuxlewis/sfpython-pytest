from app.factory.interaction import InteractionFactory

class Favorite(object):

    def __init__(self, request):
        self.request = request

    def __call__(self):
        #get interaction
        interaction = InteractionFactory.get_by_id(self.request.params['id'])

        #mark as favorited
        if interaction:
            interaction[0].events.append('favorited')
            return interaction[0].__dict__
        else:
            return {'error':'interaction not found'}






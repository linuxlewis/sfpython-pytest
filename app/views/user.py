from app.factory.user import UserFactory

class Get(object):

    def __init__(self, request):
        self.request = request

    def __call__(self):

        user = UserFactory.get_by_id(self.request.params['id'])

        if user:
            result = user[0].__dict__
        else:
            result = {'error': 'user not found'}

        return result








class User(object):

    def __init__(self):
        self.name = None
        self.id = None

    def __repr__(self):
        return 'User(%s)' % str(self.id)

    @classmethod
    def hydrate(cls, x):
        user = cls()

        user.name = x['name']
        user.id = x['id']

        return user


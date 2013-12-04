from app.model.user import User

class UserFactory(object):

    USERS = [{'id':1, 'name':'Sam'}]

    @staticmethod
    def get_by_id(id):

        return [User.hydrate(x) for x in UserFactory.USERS if x['id'] == id]



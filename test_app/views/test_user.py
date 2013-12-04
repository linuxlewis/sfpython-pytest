from app.views.user import Get

def test_get(request, user):

    # set request data
    request.params['id'] = user.id

    print user

    # test view
    view = Get(request)

    result = view()

    assert 'error' not in result
    assert result['id'] == user.id





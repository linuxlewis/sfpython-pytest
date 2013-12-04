from app.views.interaction import Favorite

def test_favorite(request, interaction):

    #set request data
    request.params['id'] = interaction.id

    print interaction

    view = Favorite(request)

    result = view()

    assert 'error' not in result
    assert result['id'] == interaction.id
    assert result['user_id'] == interaction.user_id
    assert result['listing_id'] == interaction.listing_id

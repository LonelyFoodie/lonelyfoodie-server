def get_restaurant(f_user):
    status_code, data = f_user.get('restaurant.get_restaurant', {
        'id': 'test_id'
    })

    assert status_code == 200
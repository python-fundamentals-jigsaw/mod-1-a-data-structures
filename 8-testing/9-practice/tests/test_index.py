import pytest
from practice.index import params_string

def test_params_string_coerces_dict_to_string():
    ny_params = {'location': 'New York'}
    assert params_string(ny_params) == 'location=New York', 'does not coerce dict to str'
    chicago_params = {'location': 'Chicago'}
    assert params_string(chicago_params) == 'location=Chicago', 'does not coerce dict to str'

def test_params_string_coerces_dict_greater_than_len_one_dynamically():
    ny_params = {'location': 'New York', 'limit': 50}
    assert params_string(ny_params) == 'location=New York&limit=50', 'does not coerce dict to str'
    chicago_params = {'location': 'Chicago', 'offset': 25}
    assert params_string(chicago_params) == 'location=Chicago&offset=25', 'does not coerce dict to str'

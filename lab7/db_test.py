from pymongo import MongoClient
from pymongo.collection import Collection
import pytest
from unittest.mock import Mock
from random import choice

def get_client():
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    return client['edb']['Products']

def choice_one(cursor):
    if not isinstance(cursor, Collection):
        raise TypeError(f'expected Collection. got {type(cursor)}')
    
    items = [*cursor.find({}, {"_id": 0, "name" : 1})]
    res = choice(items)
    return(res['name'])

def test_type():
    with pytest.raises(TypeError):
        choice_one('a')
        
def test_find_first():
    cursor = Mock(spec=Collection)
    cursor.find.return_value = [{'name': 'Ace Ski Boot'}]
    assert choice_one(cursor) == 'Ace Ski Boot'
    
    
if __name__ == '__main__':
    print(choice_one(get_client()))


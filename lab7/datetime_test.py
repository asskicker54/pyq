import datetime
import pytest
from unittest.mock import patch, Mock

def is_past_date(date):
    result_flag = True
    today = datetime.date.today()
    if date >= today:
        result_flag = False
    return result_flag

@pytest.mark.parametrize('inp, out', [(datetime.date(2022, 12, 31), False), (datetime.date(2022, 1, 1), True)])
def test_date(inp, out):
    date_mock = Mock(wraps=datetime.date)
    date_mock.today.return_value = datetime.date(2022, 12, 11)
    with patch('datetime.date', new=date_mock):
        assert is_past_date(inp) == out
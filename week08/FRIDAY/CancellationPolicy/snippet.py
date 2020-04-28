import datetime
from unittest.mock import Mock
friday = datetime.datetime(year=2020, month=4, day=24)
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    return (0 <= today.weekday() < 5)


datetime.datetime.today.return_value = friday
assert is_weekday()

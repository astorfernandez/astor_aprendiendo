import pytest

from ticket.dates.DateUtils import DateUtils


@pytest.mark.unit
def test_get_date_as_str_001():
    date_utils = DateUtils()
    fecha = date_utils.get_date_as_str()
    assert ('2023' in fecha)

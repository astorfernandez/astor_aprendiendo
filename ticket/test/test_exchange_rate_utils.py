import pytest

from ticket.exchange_rate.ExchangeRateUtils import ExchangeRateUtils


"""
@pytest.mark.unit
def test_basic_path():
    # prep
    exchange_rate_utils = ExchangeRateUtils()
    currency = "eu"
    
    # exec
    exhange_rate_as_float = exchange_rate_utils.get_exchange_rate_file_mode(currency)

    # assert results
    assert 145 == exhange_rate_as_float
"""


@pytest.mark.unit
def test_unknown_currency_code():
    # prep
    exchange_rate_utils = ExchangeRateUtils()
    currency = "eu"

    # assert results
    with pytest.raises(Exception) as excinfo:
        # exec
        exchange_rate_utils.get_exchange_rate_file_mode(currency)

    assert str(excinfo.value) == f"Invalid currency name: {currency}"

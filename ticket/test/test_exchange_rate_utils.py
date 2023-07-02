import pytest
import responses

from unittest.mock import patch

from ticket.exchange_rate.ExchangeRateUtils import ExchangeRateUtils
from ticket.files.FileUtils import FileUtils


MOCKED_EXCHANGE_RATE_RESPONSE_FILE = 555

MOCKED_EXCHANGE_RATE_RESPONSE_HTTP = [
    {
        'casa': {
            'compra': '260,00', 
            'venta': '270,00', 
            'agencia': '349', 
            'nombre': 'Dolar Oficial', 
            'variacion': '0,28', 
            'ventaCero': 'TRUE', 
            'decimales': '2'
        }
    }, 
    {
        'casa': {
            'compra': '488,00',
            'venta': '493,01',
            'agencia': '310',
            'nombre': 'Dolar Blue',
            'variacion': '-0,20',
            'ventaCero': 'TRUE',
            'decimales': '2'
        }
    }
]


@pytest.fixture
def mock_api_response():
    with responses.RequestsMock() as rsps:
        # Define the URL and expected response
        url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
        expected_response = MOCKED_EXCHANGE_RATE_RESPONSE_HTTP

        # Mock the GET request
        rsps.add(responses.GET, url, json=expected_response, status=200)

        yield rsps


@pytest.fixture
def mock_file_read():
    with patch.object(FileUtils, 'read_file', return_value=MOCKED_EXCHANGE_RATE_RESPONSE_FILE):
        yield


@pytest.fixture
def mock_exchange_rate_mode_http():
    with patch.object(ExchangeRateUtils, 'get_exchange_rate_mode', return_value='HTTP'):
        yield


@pytest.fixture
def mock_exchange_rate_mode_file():
    with patch.object(ExchangeRateUtils, 'get_exchange_rate_mode', return_value='FILE'):
        yield


@pytest.mark.unit
def test_exchange_rate_usd_file(mock_file_read, mock_exchange_rate_mode_file):
    # prep
    exchange_rate_utils = ExchangeRateUtils()
    currency = "usd"

    # exec
    exhange_rate_as_float = exchange_rate_utils.get_exchange_rate(currency)

    # assert results
    assert MOCKED_EXCHANGE_RATE_RESPONSE_FILE == exhange_rate_as_float


@pytest.mark.unit
def test_exchange_rate_usd_http(mock_api_response, mock_exchange_rate_mode_http):
    # prep
    exchange_rate_utils = ExchangeRateUtils()
    currency = "usd"

    # exec
    exhange_rate_as_float = exchange_rate_utils.get_exchange_rate(currency)

    # assert results
    assert 493.01 == exhange_rate_as_float


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

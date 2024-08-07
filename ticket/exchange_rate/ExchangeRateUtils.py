from ticket.files.FileUtils import FileUtils
from ticket.Constants import INPUT_PATH
from ticket.http_utils.HttpUtils import HttpUtils


EXCHANGE_RATE_MODE = 'HTTP'  # Available modes: HTTP, FILE


class ExchangeRateUtils:

    def get_exchange_rate_mode(self):
        return EXCHANGE_RATE_MODE

    def get_exchange_rate(self, currency):
        if self.get_exchange_rate_mode() == 'HTTP':
            return self.get_exchange_rate_http_mode(currency)
        elif self.get_exchange_rate_mode() == 'FILE':
            return self.get_exchange_rate_file_mode(currency)
        else:
            error_message = f"unsoported exchange rate mode: {currency}"
            raise Exception(error_message)

    def get_exchange_rate_http_mode(self, currency):
        if 'usd' == currency:
            url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
            http_utils = HttpUtils()
            dolars = http_utils.get(url)
            dolar = self.get_dolar_blue(dolars)
            return float(dolar.replace(',', '.'))
        else:
            error_message = f"Invalid currency name: {currency}"
            raise Exception(error_message)

    def get_dolar_blue(self, dolars):
        for dolar in dolars:
            if dolar['casa']['nombre'] == 'Dolar Blue':
                return dolar['casa']['venta']

    def get_exchange_rate_file_mode(self, currency):
        if 'usd' == currency:
            file_utils = FileUtils()
            exhange_rate_as_str = file_utils.read_file(INPUT_PATH, 'exchange-rate.txt')
            exhange_rate_as_float = float(exhange_rate_as_str)
            return exhange_rate_as_float
        else:
            error_message = f"Invalid currency name: {currency}"
            raise Exception(error_message)

from ticket.dates.DateUtils import DateUtils
from ticket.strings.StringUtils import StringUtils
from ticket.files.FileUtils import FileUtils
from ticket.exchange_rate.ExchangeRateUtils import ExchangeRateUtils
from ticket.Constants import OUTPUT_PATH


class Ticket:
    LINE = '---------------------------------------------'

    def __init__(self, to_file=True):
        self.to_file = to_file
        self.ticket_content = ''
        self.string_utils = StringUtils()
        self.date_utils = DateUtils()
        self.exchange_rate_utils = ExchangeRateUtils()

    def print_ticket(self, orders):
        date = self.date_utils.get_date_as_str()
        self.print_header(date)
        total = 0

        for item in orders:
            # I extract the attributes of the item
            unit_price = item['unit_price']
            amount = item['amount'] if 'amount' in item else 1
            product = item['product']

            # I do calculations
            sub_total = unit_price * amount
            total = total + sub_total
            exchange_rate = self.exchange_rate_utils.get_exchange_rate('usd')
            total_usd = total / exchange_rate
            rounded_div = round(total_usd, 2)

            # I print the line
            line_item = self.make_line(amount, product, unit_price, sub_total)
            self.print_store(line_item)

        # self.print_total_line(total)
        self.print_discount(total, rounded_div)
        self.print_total_line(total, rounded_div)
        self.print_discount(total, rounded_div)

        formated_date = date.replace('/', '-').replace(' ', '-').replace(':', '-')
        file_path = formated_date + '.txt'
        content = self.ticket_content
        if self.to_file:
            self.store(OUTPUT_PATH, file_path, content)

    def store(self, ticket_dir, file_path, content):
        ticket_dir = OUTPUT_PATH
        file_utils = FileUtils()
        file_utils.write_file(content, ticket_dir, file_path)

    def print_store(self, text):
        text_aux = text.replace('\t', '    ')
        self.ticket_content = self.ticket_content + text_aux + '\n'
        print(text)

    def print_header(self, date):
        char_amount = len(self.LINE)
        centred_date = self.string_utils.centred_text(date, char_amount)
        title = self.string_utils.centred_text('PIZZA FORA', char_amount)
        place = self.string_utils.centred_text('Liniers 1959-Tigre', char_amount)

        line_header = self.make_line('Amount', 'Detail', 'Unit.p', 'price')

        self.print_store(title)
        self.print_store(place)
        self.print_store(centred_date)
        self.print_store(self.LINE)
        self.print_store(line_header)
        self.print_store(self.LINE)

    def make_line(self, amount, detail, unit_price, price):
        amount_norm = self.string_utils.normalize_text(str(amount), 8)
        detail_norm = self.string_utils.normalize_text(detail, 19)
        unit_price_norm = self.string_utils.normalize_text(str(unit_price), 11)
        price_norm = self.string_utils.normalize_text(str(price), 10)
        line = amount_norm + detail_norm + unit_price_norm + price_norm
        return line

    def print_total_line(self, total, rounded_div):
        self.print_store(self.LINE)
        length_line = len(self.LINE)
        justified_total = self.string_utils.justify_text('$    ' + str(total), length_line)
        justified_total_usd = self.string_utils.justify_text('usd $    ' + str(rounded_div), length_line)
        self.print_store(justified_total)
        self.print_store(justified_total_usd)

    def print_discount(self, total, rounded_div):
        if total >= 1000:
            amount_characters = len(self.LINE)
            justified_text = self.string_utils.justify_text('10% de discount', amount_characters)
            self.print_store(justified_text)

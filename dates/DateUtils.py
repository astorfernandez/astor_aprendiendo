from datetime import datetime


class DateUtils:

    def get_date_as_str(self):
        today = datetime.now()
        today_as_string = today.strftime("%d/%m/%Y %H:%M:%S")
        return today_as_string

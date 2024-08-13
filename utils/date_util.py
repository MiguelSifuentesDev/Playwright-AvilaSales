from datetime import datetime


class DateUtil:
    @staticmethod
    def convert_date(date_str: str) -> str:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%a %b %d %Y')
        return formatted_date

    @staticmethod
    def get_date_id(date_str: str) -> str:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d')
        return formatted_date

    @staticmethod
    def get_month_year(date_str: str) -> str:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%Y-%m')
        return formatted_date

    @staticmethod
    def get_calendar_day(date_str: str) -> str:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%a %b %d %Y')
        return formatted_date

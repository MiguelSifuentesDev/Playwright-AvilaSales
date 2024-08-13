from playwright.sync_api import Page
from utils.date_util import DateUtil


class ExactCalendarPage:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown_calendar = page.locator("//div[@data-test-id='dropdown']")
        self.exact_calendar = page.locator("//div[@data-test-id='exact-calendar']")
        self.month_dropdown = page.locator("(//select[@ data-test-id='select-month'])[1]")

    def set_month_year(self, date):
        month_year = DateUtil.get_month_year(date)
        self.month_dropdown.click()
        self.month_dropdown.select_option(value=month_year)

    def select_calendar_date(self, date):
        calendar_date_str = DateUtil.get_calendar_day(date)
        self.dropdown_calendar.locator(f"[aria-label='{calendar_date_str}']").click()

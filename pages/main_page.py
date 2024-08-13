from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.departure_city_textbox = page.locator("//input[@data-test-id='origin-input']")
        self.destination_city_textbox = page.locator("//input[@data-test-id='destination-input']")
        self.departure_date_textbox = page.locator("//button[@data-test-id='start-date-field']")
        self.return_date_textbox = page.locator("//button[@data-test-id='end-date-field']")
        self.find_tickets_button = page.locator("//button[@data-test-id='form-submit']")

    def set_departure_city(self, city):
        self.departure_city_textbox.fill(city)

    def set_destination_city(self, city):
        self.destination_city_textbox.fill(city)

    def click_departure_date(self):
        self.departure_date_textbox.click()

    def click_return_date(self):
        self.return_date_textbox.click()

    def click_fiend_tickets(self):
        self.find_tickets_button.click()

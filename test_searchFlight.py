from playwright.sync_api import sync_playwright
import time
from pages import MainPage, SearchResultPage, ExactCalendarPage
import pytest
# import time
from pages.main_page import MainPage
# from pages.exact_calendar_page import ExactCalendarPage
# from pages.search_results_page import SearchResultPage
# from utils.date_util import DateUtil

URL = "https://www.aviasales.ru/"
TEST_DATA = {
    "departure_city": "Мехико",
    "destination_city": "Тихуана",
    "departure_date": "2024-12-10",
    "return_date": "2025-01-20"
}


@pytest.fixture
def page():
    from pages.main_page import MainPage
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_context().new_page()
        yield test_search_flights(page)


def test_search_flights(playwright: sync_playwright) -> None:
    exact_calendar_page = ExactCalendarPage(page)
    search_result_page = SearchResultPage(page)
    page.goto(URL)
    main_page.set_departure_city(TEST_DATA["departure_city"])
    main_page.set_destination_city(TEST_DATA["destination_city"])
    main_page.click_departure_date()
    exact_calendar_page.set_month_year(TEST_DATA["departure_date"])
    exact_calendar_page.select_calendar_date(TEST_DATA["departure_date"])
    exact_calendar_page.set_month_year(TEST_DATA["return_date"])
    exact_calendar_page.select_calendar_date(TEST_DATA["return_date"])
    main_page.click_fiend_tickets()
    assert search_result_page.has_results(), "No results found"
    assert (search_result_page.is_matched_criteria(TEST_DATA["departure_city"], TEST_DATA["departure_date"],
                                                   TEST_DATA["destination_city"], TEST_DATA["return_date"]),
            "No matched search criteria")
    
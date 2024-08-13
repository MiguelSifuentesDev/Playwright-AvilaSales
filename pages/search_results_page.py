from playwright.sync_api import Page


class SearchResultPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_result = page.get_by_test_id("ticket-preview")

    # def search_faster_flight(self):
    #     flights = self.search_result.get_by_test_id("ticket-preview").element_handle()
    #     for flight in flights.query_selector():
    #         print(flight)

    def is_matched_criteria(self, departure_city: str, departure_date: str, return_city: str, return_date: str) -> bool:
        flight_info = self.search_result.first
        departure_info = flight_info.get_by_test_id("origin-endpoint").first
        return_info = flight_info.get_by_test_id("origin-endpoint").last
        has_departure_info = departure_info.filter(has_text=departure_city).filter(has_text=departure_date).count() > 0
        has_return_info = return_info.filter(has_text=return_city).filter(has_text=return_date).count() > 0
        return has_departure_info and has_return_info

    def has_results(self):
        return self.search_result.count() > 0

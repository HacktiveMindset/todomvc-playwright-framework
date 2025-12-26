import allure
from utils.helpers import load_test_data
data=load_test_data()
@allure.feature("UI Validation")
def test_TC026_to_TC033(page):
    page.goto(data["base_url"])
    assert page.locator("h1").text_content()=="todos"
    assert page.locator(".new-todo").is_visible()

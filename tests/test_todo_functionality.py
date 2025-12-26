import allure
from pages.TodoPage import TodoPage
from utils.helpers import load_test_data
data=load_test_data()
@allure.feature("Todo Functionality")
def test_TC001_to_TC016(page):
    todo=TodoPage(page)
    todo.open(data["base_url"])
    todo.add_todo(data["add_todo"]["single"])
    todo.add_todo(data["add_todo"]["multiple"][0])
    todo.add_todo(data["add_todo"]["special"])
    todo.add_todo(data["add_todo"]["long"])
    assert todo.get_active_count()==4

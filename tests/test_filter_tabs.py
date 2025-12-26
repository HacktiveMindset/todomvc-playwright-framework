import allure
from pages.TodoPage import TodoPage
from utils.helpers import load_test_data
data=load_test_data()
@allure.feature("Filter Tabs")
def test_TC017_to_TC025(page):
    todo=TodoPage(page)
    todo.open(data["base_url"])
    todo.add_todo(data["add_todo"]["multiple"][0])
    todo.add_todo(data["add_todo"]["multiple"][1])
    todo.toggle_todo(0)
    todo.click_active()
    assert page.locator(todo.todo_items).count()==1
    todo.click_completed()
    assert page.locator(todo.todo_items).count()==1
    todo.click_all()
    assert page.locator(todo.todo_items).count()==2

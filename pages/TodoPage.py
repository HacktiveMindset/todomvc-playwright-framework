from pages.BasePage import BasePage
class TodoPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.todo_input=".new-todo"
        self.todo_items=".todo-list li"
        self.todo_labels=".todo-list li label"
        self.todo_count=".todo-count strong"
        self.clear_completed_btn=".clear-completed"
        self.all_tab="a[href='#/']"
        self.active_tab="a[href='#/active']"
        self.completed_tab="a[href='#/completed']"
    def add_todo(self,text):
        self.page.fill(self.todo_input,text)
        self.page.keyboard.press("Enter")
    def toggle_todo(self,index):
        self.page.locator(self.todo_items).nth(index).locator("input.toggle").click()
    def delete_todo(self,index):
        item=self.page.locator(self.todo_items).nth(index)
        item.hover()
        item.locator("button.destroy").click()
    def clear_completed(self):
        if self.page.locator(self.clear_completed_btn).is_visible():
            self.page.click(self.clear_completed_btn)
    def get_active_count(self):
        return int(self.page.text_content(self.todo_count))
    def click_all(self):
        self.page.click(self.all_tab)
    def click_active(self):
        self.page.click(self.active_tab)
    def click_completed(self):
        self.page.click(self.completed_tab)

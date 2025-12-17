from playwright.sync_api import Page, Locator

class Base:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_menu(self) -> None:
       menu = self.page.get_by_role("link", name="menu")
       menu.click()
       self.page.locator("css=[href='/'].router-link-active router-link-exact-active").wait_for()
       
    def get_cart(self) -> Locator:
        return self.page.get_by_role("link", name="Cart Page")

    def navigate_to_cart(self) -> None:
        cart = self.get_cart()
        cart.click()
        self.page.locator("css=[href='/cart'].router-link-active router-link-exact-active").wait_for()
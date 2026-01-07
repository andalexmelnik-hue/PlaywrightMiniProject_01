import logging
from playwright.sync_api import Page, Locator, ConsoleMessage

def get_logger() -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('Error_TA.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

class Base:
    def __init__(self, page: Page):
        self.page = page
        self.log = get_logger()
        
        self.page.on("console", self._handle_console)

    def _handle_console(self, msg: ConsoleMessage) -> None:
        if msg.type.lower() in ('error', 'warning'):
            self.log.error(f"{self.page.url} {msg.type}: {msg.text}")
    
    def goto(self, url: str, **kwargs) -> None:
        self.page.goto(url, wait_until="networkidle", **kwargs)

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
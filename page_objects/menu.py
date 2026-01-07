from page_objects.base import Base
from playwright.sync_api import Route
from contextlib import contextmanager
import json

class Menu(Base):

    def get_coffee_item(self, coffee_name: str):
        return self.page.get_by_label(coffee_name, exact=True)
    
    def add_coffee(self, coffee_name: str) -> None:
        return self.get_coffee_item(coffee_name).click()

    def get_coffee_price(self, coffee_name: str) -> float:
        items = self.page.get_by_role("listitem")
        item = items.filter(has=self.get_coffee_item(coffee_name))
        price = item.locator("small").inner_text().strip().replace("$", "")
        return float(price)

    def get_price(self) -> str:
        return self.page.get_by_role("button", name="Proceed to checkout").inner_text().strip()
    
    def get_nah_button(self):
        return self.page.get_by_role("button", name="Nah, I'll skip.")
    
    def get_context(self):
        return self.page.context
    
    @contextmanager
    def intercept(self, status):
        # handler closure that captures `status` and delegates to the instance method
        def _handler(route: Route):
            return self._intercept_handler(route, status)

        self.page.route("**/list.json", handler=_handler)
        try:
            yield
        finally:
            # unregister the same handler
            self.page.unroute("**/list.json", handler=_handler)

    def _intercept_handler(self, route: Route, status) -> None:
        if status == 500:
            route.fulfill(
                status=500,
                json=[{
                    "name": "Coffee API Error",
                }],
                headers={"Content-Type": "text/plain"}
            )
        elif status == 200:
            route.fulfill(
                status=200,
                json=[{
                    "name": "Espresso 1",
                    "price": 11,
                    "recipe": [
                        { "name": "espresso", "quantity": 100 }
                    ]
                }],
                headers={"Content-Type": "application/json"}
            )
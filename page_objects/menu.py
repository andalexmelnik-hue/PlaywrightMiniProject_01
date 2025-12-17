from page_objects.base import Base

class Menu(Base):

    def get_coffee_item(self, coffee_name: str):
        return self.page.get_by_label(coffee_name, exact=True)
    
    def add_coffee(self, coffee_name: str) -> None:
        return self.get_coffee_item(coffee_name).click()

    def get_coffee_price(self, coffee_name: str) -> str:
        items = self.page.get_by_role("listitem")
        item = items.filter(has=self.get_coffee_item(coffee_name))
        price = item.locator("small").inner_text().strip().replace("$", "")
        return float(price)

    def get_price(self) -> str:
        return self.page.get_by_role("button", name="Proceed to checkout").inner_text().strip()

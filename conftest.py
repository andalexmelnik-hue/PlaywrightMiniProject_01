from pytest import fixture
from playwright.sync_api import Page
from page_objects.menu import Menu
from typing import Generator

@fixture
def auth(page: Page) -> Generator[Page, None, None]:
    page.goto("/")
    yield page
    
@fixture
def menu(auth: Page) -> Generator[Menu, None, None]:
    yield Menu(auth)
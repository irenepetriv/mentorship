#pages/base_page.py

from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page) -> object:
        self.page = page

    def navigate(self, url: str):
        """Navigate to a specified URL."""
        self.page.goto(url)

    def get_element(self, locator: str):
        """Return an element by its locator (CSS or XPath)."""
        return self.page.locator(locator)

    def click(self, locator):
        if isinstance(locator, str):
            self.get_element(locator).click()
        elif isinstance(locator, Locator):
            locator.click()

    def is_visible(self, locator: str or Locator) -> bool:
        locator = locator if isinstance(locator, Locator) else self.locator(locator)
        return locator.is_visible()

    def fill_input(self, locator: str, value: str):
        """Fill input with a value."""
        self.get_element(locator).fill(value)

    def check(self, locator: str):
        self.check(locator)

    def get_text(self, locator: str) -> str:
        """Get text content of an element."""
        return self.get_element(locator).text_content()

    def is_element_visible(self, locator: str) -> bool:
        """Check if an element is visible."""
        return self.get_element(locator).is_visible()

    def wait_for_element(self, locator: str, timeout: int = 5000):
        """Wait for an element to appear."""
        self.page.wait_for_selector(locator, timeout=timeout)

    def take_screenshot(self, path: str):
        """Take a screenshot and save to the specified path."""
        self.page.screenshot(path=path)


    def locator(self, locator: str, wait_for_locator: bool = True):
        if wait_for_locator:
            self.page.locator(locator).first.wait_for(state="attached")
            return self.page.locator(locator)
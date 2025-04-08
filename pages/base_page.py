from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page #dunno if it needed, used to interact with single tab in browser. Read about page constructor

    def navigate(self, url: str):
        """Navigate to a specified URL."""
        self.page.goto(url) #it is needed,it returns the main resource response so that ve could work with it. Also, it may ne used to check the permissions to pages

    def locator(self, locator: str):
        """Return an element by its locator (CSS or XPath)."""
        return self.page.locator(locator) # returns element of the page, locator. It finds element matching the specified selector. We just use it to resolve DOM element. I guess NOT needed.

    def click(self, locator: str):
        """Click an element."""
        self.locator(locator).click() #тут перевикористовується get_element з вище? якщо ми робимо get element як вище, то не знаю, чи потрібно click? напевно потрібно, щоб кудись провалитися чи кли йде серія дій?

    def fill(self, locator: str, value: str):
        """Fill input with a value."""
        self.locator(locator).fill(value) # вставляє якесь значення в input field.  Тестити валідацію?

    def get_text(self, locator: str) -> str:
        """Get text content of an element."""
        return self.locator(locator).text_content() # The textContent property of the Node interface represents the text content of the node and its descendants. What the hell it is?

    def is_element_visible(self, locator: str) -> bool:
        """Check if an element is visible."""
        return self.locator(locator).is_visible() # Returns whether the element is visible. не знаю нащо це?

    def wait_for_element(self, locator: str, timeout: int = 5000):
        """Wait for an element to appear."""
        self.page.wait_for_selector(locator, timeout=timeout) #If target element already satisfies the condition, the method returns immediately. Otherwise, waits for up to timeout milliseconds until the condition is met.
     # нам для проекту напевно такого не треба)
    def take_screenshot(self, path: str):
        """Take a screenshot and save to the specified path."""
        self.page.screenshot(path=path)  # не потрібно
    def all(self, locator: str):
        """Return a list of elements that match the given locator."""
        elements = self.page.locator(locator).all()  # Use `.all()` to collect all elements that match the selector.
        return elements  # Return the list of elements

    def all_text_contents(self, locator: str):
        """Return the text content of all matching elements."""
        return self.page.locator(locator).all_text_contents()  # Directly return the text content of matching nodes.
    def blur_element(self, locator: str):
        """Simulate the blur (losing focus) of an element."""
        self.page.locator(locator).blur()  # Simulate blur event on the element

    def check_element(self, locator: str, timeout: int = 30000):
        """Simulate checking a checkbox or selecting a radio button with a timeout."""
        self.page.locator(locator).check(timeout=timeout)  # Timeout in milliseconds
    def clear(self, locator: str):
        """Clear input of a field."""
        self.locator(locator).clear() # чистить поле вводу, може бути корисним, якщо потрібно почистити поле, перед водом іншого значення.
    def count_elements(self, locator: str) -> int:
        """Clear input of a field."""
        return self.page.locator(locator).count()
    def dblclick(self, locator: str):
        """Perform a double-click action on the specified element."""
        self.locator(locator).dblclick()
    def dispatch_event(self, locator: str, event_type: str):
        """Dispatch an event on a specified element."""
        self.page.locator(locator).dispatch_event(event_type)

    def drag_to(self, source_locator: str, target_locator: str):
        """Drag an element from source to target."""
        source = self.page.locator(source_locator)
        target = self.page.locator(target_locator)
        source.drag_to(target)

    def match_with_evaluate(self, locator: str, match_script: str):
        """Evaluate a JavaScript expression to match an element's property or state."""
        # Use `evaluate()` to run JavaScript to check if the element matches the provided condition.
        element = self.locator(locator)  # Get the element by locator.
        result = element.evaluate(match_script)  # Evaluate the script on the element.
        return result  # Return the result of the evaluation.

    def match_all_with_evaluate(self, locator: str, match_script: str):
        """Evaluate a JavaScript expression on all elements that match the locator."""
        # Get all elements matching the locator.
        elements = self.locator(locator)  # Retrieve all elements by the locator.

        # Use `evaluate_all()` to run the JavaScript on each of the elements.
        results = elements.evaluate_all(match_script)  # Evaluate the script on each element.

        return results

    def match_with_evaluate_handle(self, locator: str, match_script: str):
        """Evaluate a JavaScript expression and return the handle (a reference to the underlying element or the result of the evaluation)to the element or result."""
        # Get the element by the locator.
        element = self.locator(locator)  # Retrieve the element by the locator.

        # Use `evaluate_handle()` to run the JavaScript and get a handle to the result.
        handle = element.evaluate_handle(match_script)  # Evaluate the script and get the handle.

        return handle

    def match_with_fill(self, locator: str, text: str):
        """Fill the input field and check if it matches the expected text."""
        element = self.locator(locator)  # Retrieve the input field by the locator.
        element.fill(text)  # Use the `fill()` method to input the text into the field.
        return element  # Return the element for further verification (optional)
    def match_with_filter(self, locator: str, filter_script: str):
        """Filter elements based on the provided JavaScript condition."""
        elements = self.locator(locator)  # Retrieve all elements matching the locator.
        filtered_elements = elements.filter(filter_script)  # Filter the elements using the provided JavaScript condition.
        return filtered_elements  # Return the filtered elements

    def match_with_focus(self, locator: str, text: str):
        """Focus on the element and fill the text."""
        element = self.locator(locator)  # Retrieve the input field by the locator.
        element.focus()  # Focus on the element (typically an input field).
        element.fill(text)  # Fill the input field with the provided text.
        return element  # Return the element for further verification (optional)

    def iframe(self, iframe_locator: str):
        """Locate an iframe and return a frame context to interact with elements inside."""
        iframe_element = self.page.locator(iframe_locator)  # Locate the iframe using a selector (CSS or XPath)
        iframe = iframe_element.frame()  # Switch the context to the iframe
        return iframe  # Return the frame context to interact with elements inside the iframe.

    def get_attribute(self, element_locator: str, attribute: str):
        """Retrieve the value of an attribute from an element. if it is href then attribute holds the URL the link points"""
        element = self.page.locator(element_locator)  # Locate the element on the page
        return element.get_attribute(attribute)  # Get the value of the specified attribute.

    def get_by_alt_text(self, alt_text: str):
        """Find an element by its alt text (typically used for images)."""
        return self.page.locator(f'img[alt="{alt_text}"]')  # Locate the image with the given alt text.

    def get_by_label(self, label_text: str):
        """Find a form control element by its associated label's text."""
        # Use the 'for' attribute of the label to locate the associated input or form element
        return self.page.locator(f'label:text("{label_text}") >> input, textarea, select, button')
        # This will locate the associated input, textarea, select, or button based on the label's text.

    def get_by_placeholder(self, placeholder_text: str):
        """Find an input or textarea element by its placeholder text."""
        return self.page.locator(f'input[placeholder="{placeholder_text}"], textarea[placeholder="{placeholder_text}"]')
        # Locate input or textarea with the given placeholder text.

    def get_by_role(self, role: str, name: str = None):
        """Find an element by its ARIA role, and optionally by its accessible name."""
        if name:
            return self.page.locator(
                f'[role="{role}"][name="{name}"]')  # Optional: use the accessible name if provided.
        return self.page.locator(f'[role="{role}"]')  # Find an element by its ARIA role.

    def get_by_test_id(self, test_id: str):
        """Find an element by its custom data-testid attribute."""
        return self.page.locator(f'[data-testid="{test_id}"]')  # Locate element with the given test id.

    def get_by_text(self, text: str):
        """Find an element by its inner text."""
        return self.page.locator(f'text="{text}"')  # Locate element by its inner text.

    def get_by_title(self, title_text: str):
        """Find an element by its title attribute."""
        return self.page.locator(f'[title="{title_text}"]')  # Locate element with the given title text.

    def hover(self, locator: str):
        """Hover over an element."""
        self.locator(locator).hover()  # Hover the mouse over the element.

    def highlight(self, locator: str):
        """Highlight an element by changing its background color."""
        element = self.locator(locator)
        element.evaluate(
            'element => element.style.backgroundColor = "yellow"')  # Change the background color to yellow for highlighting.

    def input_value(self, locator: str):
        """Get the current value of an input field."""
        return self.locator(locator).input_value()  # Return the value of an input element.

    def is_checked(self, locator: str):
        """Check if a checkbox or radio button is checked."""
        return self.locator(locator).is_checked()  # Return if the checkbox or radio button is checked.

    def is_disabled(self, locator: str):
        """Check if an element is disabled."""
        return self.locator(locator).is_disabled()  # Return if the element is disabled.

    def is_editable(self, locator: str):
        """Check if an element is editable."""
        return self.locator(locator).is_editable()  # Return if the element is editable.

    def is_enabled(self, locator: str):
        """Check if an element is enabled."""
        return self.locator(locator).is_enabled()  # Return if the element is enabled.

    def is_hidden(self, locator: str):
        """Check if an element is hidden (invisible)."""
        return self.locator(locator).is_hidden()  # Return if the element is hidden.

    def is_visible(self, locator: str):
        """Check if an element is visible."""
        return self.locator(locator).is_visible()

    def press(self, locator: str, key: str):
        """Press a key on an element (e.g., Enter, Backspace, etc.)."""
        self.locator(locator).press(key)  # Press the given key on the element.

    def press_sequentially(self, locator: str, keys: list):
        """Press a sequence of keys on an element."""
        for key in keys:
            self.locator(locator).press(key)  # Sequentially press each key.

    def scroll_into_view_if_needed(self, locator: str):
        """Scroll the element into view if it's not already visible."""
        self.locator(locator).scroll_into_view_if_needed()  # Scroll the element into view.

    def select_option(self, locator: str, option_value: str):
        """Select an option from a dropdown by value."""
        self.locator(locator).select_option(value=option_value)  # Select option by value.

    def select_text(self, locator: str, text: str):
        """Select text in an input field or text area."""
        self.locator(locator).select_text(text)  # Select text inside the input element.

    def set_checked(self, locator: str):
        """Check a checkbox or toggle a switch."""
        self.locator(locator).set_checked(True)  # Set checkbox to checked.

    def set_input_files(self, locator: str, file_paths: list):
        """Set files for an input field (e.g., file upload)."""
        self.locator(locator).set_input_files(*file_paths)  # Set the files for file input.

    def tap(self, locator: str):
        """Tap an element (usually for mobile interactions)."""
        self.locator(locator).tap()  # Tap the element (like clicking on mobile).

    def text_content(self, locator: str):
        """Get the text content of an element."""
        return self.locator(locator).text_content()  # Get the inner text content of the element.

    def uncheck(self, locator: str):
        """Uncheck a checkbox or toggle a switch."""
        self.locator(locator).set_checked(False)  # Uncheck the checkbox.

    def wait_for(self, locator: str, timeout: int = 30000):
        """Wait for an element to be present, visible, or stable."""
        self.locator(locator).wait_for(timeout=timeout)  # Wait for the element to meet the condition.

    def content_frame(self, locator: str):
        """Get the content frame (useful for iframe)."""
        return self.locator(locator).content_frame()  # Retrieve the content frame of the element.

    def first(self, locator: str):
        """Get the first matching element from a collection."""
        return self.locator(locator).first  # Get the first matching element from a list.

    def last(self, locator: str):
        """Get the last matching element from a collection."""
        return self.locator(locator).last  # Get the last matching element from a list.

    def type(self, locator: str, text: str):
        """Type text into an input field."""
        self.locator(locator).type(text)  # Type the given text into the element.










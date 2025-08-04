from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    product_title = (By.CLASS_NAME, "title")
    product_items = (By.CLASS_NAME, "inventory_item")
    add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    # Actions
    def get_page_title(self):
        return self.driver.find_element(*self.product_title).text

    def get_all_products(self):
        return self.driver.find_elements(*self.product_items)

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        if buttons:
            buttons[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.mark.usefixtures("driver")
class TestProductPage:

    def login(self, driver):
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

    def test_product_page_title(self, driver):
        self.login(driver)
        product = ProductPage(driver)
        assert product.get_page_title() == "PRODUCTS"

    def test_all_products_are_visible(self, driver):
        self.login(driver)
        product = ProductPage(driver)
        items = product.get_all_products()
        assert len(items) > 0, "No products found on the page"

    def test_add_product_to_cart(self, driver):
        self.login(driver)
        product = ProductPage(driver)
        product.add_first_product_to_cart()
        product.go_to_cart()
        assert "cart" in driver.current_url


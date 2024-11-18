import pytest
from pages.login import Login
from pages.products import Products
from pages.cart import Cart

@pytest.fixture
def login(driver):
    """
    Fixture para iniciar sesión antes de cada test.
    """
    driver.get("https://www.saucedemo.com/")
    login = Login(driver)
    login.login("standard_user", "secret_sauce")
    yield

def test_add_single_product_to_cart(driver, login):
    products = Products(driver)
    products.add_product_to_cart(0)
    cart_count = products.get_cart_count()
    assert cart_count == 1

def test_add_multiple_products_to_cart(driver, login):
    products = Products(driver)
    products.add_product_to_cart(0)
    products.add_product_to_cart(1)
    cart_count = products.get_cart_count()
    assert cart_count == 3 # Deberá de ser 2 pero le pongo 3 para que falle
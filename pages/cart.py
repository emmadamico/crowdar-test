from selenium.webdriver.common.by import By
from .base import Base

class Cart(Base):
    REMOVE_BUTTONS = (By.CLASS_NAME, "cart_button")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def remove_product_from_cart(self, p_index=0):
        buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        if p_index < len(buttons):
            buttons[p_index].click()

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)
    
    def remove_all_products(self):
        """
        Elimina todos los productos del carrito, si existen.
        """
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        for item in cart_items:
            remove_button = item.find_element(*self.REMOVE_BUTTONS)
            remove_button.click()
    
    def empty_cart(self):
        """
        Navega al carrito y elimina todos los productos.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.remove_all_products()
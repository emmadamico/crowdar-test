from selenium.webdriver.common.by import By
from .base import Base

class Products(Base):
    PRODUCT_ADD_BUTTONS = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_product_to_cart(self, p_index=0):
        buttons = self.driver.find_elements(*self.PRODUCT_ADD_BUTTONS)
        if p_index < len(buttons):
            buttons[p_index].click()

    def get_cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except:
            return 0
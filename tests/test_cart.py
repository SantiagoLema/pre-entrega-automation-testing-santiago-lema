from selenium.webdriver.common.by import By
from selenium import webdriver


def test_cart(login_in_driver):
    try:
        driver = login_in_driver
        driver.implicitly_wait(5)

        # Busca un articulo y lo agrega al carrito
        first_item = driver.find_element(By.CSS_SELECTOR, ".inventory_item")
        first_item_name = first_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        first_item.find_element(By.TAG_NAME, "button").click()   

        # Verifica badge del carrito = 1
        badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        assert badge == "1", f"El contador del carrito es {badge} (se esperaba 1)"

        # Confirmación de producto en el carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_name = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
        assert cart_name == first_item_name, "El producto del carrito no coincide"

        print("Test OK")
    finally:
        driver.quit()
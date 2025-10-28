from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        # Verificar que el titulo sea "Swag Labs"
        assert driver.title == "Swag Labs"

        # Verifica la existencia de productos en el inventario
        products = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()
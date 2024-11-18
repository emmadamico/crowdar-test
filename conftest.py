"""
Archivo de configuración de PyTest.
Su función es contener la configuración de los fixtures que estarán disponibles 
para todos los tests. 
Se incluye:
 - la configuración para Chrome y Firefox
 - el código para las capturas de pantalla
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Navegador para correr los casos. Por defecto es chrome, pero se puede hacer uso de firefox también."
    )

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="function")
def driver(browser):
    """
    Agrego la opción para ejecutar en modo headless para que el navegador se ejecute
    en segundo plano sin mostrar una interfaz gráfica.
    """
    if browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--headless")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Se ejecuta el reporte luego de cada test.
    Si el test falla, entonces se genera un screenshot y el mismo se guarda en la carpeta screenshots
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(BASE_DIR, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)
            
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest

@pytest.fixture(scope="class")
def base_url():
    return "https://reqres.in/api"

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class")
def driver(browser):
    if browser == "firefox":
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Не поддерживаемый браузер: {browser}")
    yield driver
    driver.quit()





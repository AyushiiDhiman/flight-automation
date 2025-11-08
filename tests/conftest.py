import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import json
from pathlib import Path


@pytest.fixture(scope="session")
def config():
    cfg_path = Path(__file__).parent.parent / "data" / "testdata.json"
    with open(cfg_path) as f:
        return json.load(f)


@pytest.fixture
def driver(request: pytest.FixtureRequest):

    
    chrome_driver_path = r"C:\Users\dell\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"

    
    options = Options()
    options.add_argument("--window-size=1400,900")
    options.add_argument("--disable-gpu")

    
    service = ChromeService(executable_path=chrome_driver_path)

   
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

   
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: quick smoke tests")





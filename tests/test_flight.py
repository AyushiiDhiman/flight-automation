import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_flight_booking(driver, config):
    driver.get(config["url"])

    
    origin_dropdown = Select(driver.find_element(By.NAME, "fromPort"))
    origin_dropdown.select_by_visible_text(config["origin"])

   
    destination_dropdown = Select(driver.find_element(By.NAME, "toPort"))
    destination_dropdown.select_by_visible_text(config["destination"])

   
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    
    assert "Flights from" in driver.page_source



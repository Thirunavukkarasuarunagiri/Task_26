from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.imdb.com/search/name")

    def fill_search_criteria(self, name, birth_year, profession):
        name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search_name")))
        name_input.clear()
        name_input.send_keys(name)

        birth_year_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search_birth_year")))
        birth_year_input.clear()
        birth_year_input.send_keys(birth_year)

        profession_select = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search_primary_profession")))
        profession_select.click()
        profession_option = profession_select.find_element(By.XPATH, f"//option[text()='{profession}']")
        profession_option.click()

    def perform_search(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
        search_button.click()

import pytest
from selenium import webdriver
from imdb_search_page import IMDbSearchPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_imdb_search(browser):
    imdb_search_page = IMDbSearchPage(browser)
    imdb_search_page.fill_search_criteria("Tom Cruise", "1962", "Actor")
    imdb_search_page.perform_search()
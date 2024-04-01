# test_selenium.py

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  # Replace with appropriate WebDriver
    yield driver
    driver.quit()


def test_upload_csv(browser):
    browser.get("http://localhost:5000")
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(
        "/home/murage/Documents/school/APT3010/project/flask-project/app/static/sample_schedule.csv")

    upload_button = browser.find_element(By.CSS_SELECTOR,
                                         "button[type='submit']")
    upload_button.click()
    time.sleep(2)
    h1_element = browser.find_element(By.CSS_SELECTOR, "h1")
    assert "Lab Schedule" in h1_element.text


def test_schedule_page_content(browser):
    tables = browser.find_elements(By.CSS_SELECTOR, "table")
    table_headers = set()
    expected_headers = ["Class", "Lab", "Course Name", "Faculty"]
    for table in tables:
        headers = table.find_elements(By.CSS_SELECTOR, "th")
        for header in headers:
            table_headers.add(header.text)
    assert len(table_headers) == len(expected_headers)

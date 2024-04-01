import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

@pytest.fixture
def browser():
    # Set up the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown: Close the WebDriver
    driver.quit()

def test_download_sample_schedule(browser):
    # Navigate to the web page
    browser.get("http://localhost:5000")  # Replace with the actual URL

    # Locate the download button element
    download_button = browser.find_element(By.XPATH, "//a[contains(text(), 'Download Sample Schedule')]")

    # Simulate a click on the download button
    download_button.click()

    # Wait for the download process to complete (adjust the sleep duration as needed)
    time.sleep(2)

    # Verify that the file has been downloaded
    download_path = "/home/murage/Downloads"  # Specify the path to the download directory
    downloaded_file = os.path.join(download_path, "sample_schedule.csv")
    assert os.path.exists(downloaded_file), "Sample schedule file was not downloaded"

      # Remove the downloaded file
    os.remove(downloaded_file)
    assert not os.path.exists(downloaded_file), "Sample schedule file was not deleted"

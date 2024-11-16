from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Use the Service object to specify the path to chromedriver
service = Service(ChromeDriverManager().install())  # This installs the correct chromedriver version automatically

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open the specified URL
driver.get("https://website.com")

# Continuously reload the page every 2 seconds
while True:
    time.sleep(2)  # Wait for 2 seconds
    driver.refresh()  # Reload the page

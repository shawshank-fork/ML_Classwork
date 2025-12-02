from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Setup Chrome browser with automatic driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Website to scrape
url = "https://quotes.toscrape.com/js/"  # Dynamic JavaScript-loaded site

driver.get(url)

# Wait for JavaScript content to load
time.sleep(2)

# Extract quotes using XPath or class selectors
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

print("Extracted Quotes from Website:\n")

for i in range(len(quotes)):
    print(f"{quotes[i].text} — {authors[i].text}")

driver.quit()
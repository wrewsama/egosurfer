from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://schedule.hololive.tv/")

driver.implicitly_wait(10)
driver.save_screenshot("screenshot.png")
driver.quit()
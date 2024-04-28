from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def getDriver() -> webdriver.Chrome:
    # Starting up selenium web driver.
    chrome_browser_options = Options()
    chrome_browser_options.add_experimental_option("useAutomationExtension", False)
    chrome_browser_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )
    chrome_browser_options.add_argument("--ignore-ssl-errors=yes")
    chrome_browser_options.add_argument("--ignore-certificate-errors")
    chrome_browser_options.add_argument("--start-fullscreen")
    driver: webdriver.Chrome = webdriver.Chrome(options=chrome_browser_options)
    return driver

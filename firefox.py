from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#!/usr/bin/env python
def create_driver():
    options = Options()
    options.headless = True
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)

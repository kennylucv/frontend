
# control Chorme with selenium

from selenium import webdriver

for i in range(6):
    driver = webdriver.Chrome()
    # open browser and go to Google.ca
    driver.get('http://frontend-http-route-dev-env.127.0.0.1.nip.io/login?returnUrl=%2F')


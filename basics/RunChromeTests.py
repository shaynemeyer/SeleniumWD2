from selenium import webdriver
import os


class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "/Users/Shared/Git/SeleniumProject/lib/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate FF Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provide URL
        driver.get("http://www.letskodeit.com")

ff = RunChromeTests()
ff.test()

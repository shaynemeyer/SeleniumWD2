from selenium import webdriver
import os


class RunSafariTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        serverLocation = "/Users/Shared/Git/SeleniumProject/lib/selenium-server-standalone-3.4.0.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation
        # Instantiate FF Browser Command
        driver = webdriver.Safari()
        # Open the provide URL
        driver.get("http://www.letskodeit.com")

ff = RunSafariTests()
ff.test()

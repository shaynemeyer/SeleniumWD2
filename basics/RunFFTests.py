from selenium import webdriver


class RunFFTests():

    def test(self):
        # Instantiate FF Browser Command
        driver = webdriver.Firefox(executable_path=r'/Users/Shared/Git/SeleniumProject/lib/geckodriver')

        # Open the provide URL
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.test()

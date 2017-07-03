from selenium import webdriver


class FindByXpathCss():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path=r'/Users/Shared/Git/SeleniumProject/lib/geckodriver')
        driver.get(base_url)
        element_by_xpath = driver.find_element_by_xpath("//*[@id='name']")

        if element_by_xpath is not None:
            print("found element with xpath by name")

        element_by_css = driver.find_element_by_css_selector("#displayed-text")

        if element_by_css is not None:
            print("found element by css")

ff = FindByXpathCss()
ff.test()

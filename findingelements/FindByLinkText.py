from selenium import webdriver


class FindByLinkText():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path=r'/Users/Shared/Git/SeleniumProject/lib/geckodriver')
        driver.get(base_url)

        element_by_link_text = driver.find_element_by_link_text("Login")

        if element_by_link_text is not None:
            print("found element by link text")

        element_by_partial_link_text = driver.find_element_by_partial_link_text("Pract")

        if element_by_partial_link_text is not None:
            print("found element by partial link text")

ff = FindByLinkText()
ff.test()
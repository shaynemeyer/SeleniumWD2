from selenium import webdriver


class FindByIdName():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path=r'/Users/Shared/Git/SeleniumProject/lib/geckodriver')
        driver.get(base_url)
        element_by_id = driver.find_element_by_id("name")

        if element_by_id is not None:
            print("found element with id=name")

        element_by_name = driver.find_element_by_name('show-hide')

        if element_by_name is not None:
            print("found element by name")

ff = FindByIdName()
ff.test()

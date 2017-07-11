from selenium import webdriver


class FindByClassName():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path=r'/Users/Shared/Git/SeleniumProject/lib/geckodriver')
        driver.get(base_url)

        element_by_class_name = driver.find_element_by_class_name("displayed-class")

        if element_by_class_name is not None:
            print("found element by class name")

        element_by_tag_name = driver.find_element_by_tag_name("a")

        if element_by_tag_name is not None:
            print("found element by tag name")

ff = FindByClassName()
ff.test()
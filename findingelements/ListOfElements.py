from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements():

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=r'/Users/Shared/Git/SeleniumProject/lib/geckodriver')
        driver.get(base_url)

        element_list_by_class_name = driver.find_elements_by_class_name("inputs")
        length1 = len(element_list_by_class_name)

        if element_list_by_class_name is not None:
            print("ClassName -> Size of the list is: " + str(length1))

        element_list_by_tag_name = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(element_list_by_tag_name)

        if element_list_by_tag_name is not None:
            print("TagName -> Size of the list is: " + str(length2))

ff = ListOfElements()
ff.test()
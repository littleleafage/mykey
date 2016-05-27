import unittest
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt
class DDTSimpleTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.baidu.com/")

    # specify test data using @data decorator
    @data(("Selenium", 1), ("Python", 2))
    @unpack

    def test_search(self, search_text, TestCase_ID):

        print " Search Text " + search_text
        print " Search TestCase ID " + str(TestCase_ID)

        # get the search textbox
        self.search_field = self.driver.find_element_by_name("wd")
        self.search_field.clear()

        # enter search keyword and submit.
        # use search_text argument to input data
        self.search_field.send_keys(search_text)
        self.search_field.submit()

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

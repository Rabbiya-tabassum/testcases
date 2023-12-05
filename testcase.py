from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class TestWebApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_homepage_loads(self):
        self.driver.get("https://3.93.47.246/")
        self.assertIn("Your Web Application", self.driver.title)

    def test_login(self):
        self.driver.get("https://3.93.47.246/login")
        
        username_input = self.driver.find_element_by_id("username")
        password_input = self.driver.find_element_by_id("password")
        submit_button = self.driver.find_element_by_id("submit")
        
        username_input.send_keys("redninjaz")
        password_input.send_keys("abcdef@#$")
        submit_button.click()

        
        self.assertIn("dashboard", self.driver.current_url)

    def test_search_functionality(self):
        self.driver.get("https://3.93.47.246/dashboard")
        
        search_input = self.driver.find_element_by_id("search")
        search_button = self.driver.find_element_by_id("search_button")

        search_input.send_keys("search_query")
        search_button.click()

        self.assertIn("search_results", self.driver.page_source)

    def test_logout(self):
        self.driver.get("https://3.93.47.246/dashboard")
        logout_button = self.driver.find_element_by_id("logout_button")
        logout_button.click()

      
        self.assertIn("login", self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

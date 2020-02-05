import time
import unittest
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('http://www.python.org')
        self.assertIn('Python', self.driver.title)
        self.driver.find_element_by_link_text('Downloads').click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'widget-title')
            )
        )
        self.assertEqual('Looking for a specific release?', element.text)

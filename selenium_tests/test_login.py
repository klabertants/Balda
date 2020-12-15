from selenium.webdriver import Safari
import unittest
import time
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = Safari()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(2048, 1280)

    def test_registration(self):
        driver = self.driver

        driver.get('http://127.0.0.1:8000/login/')

        username = driver.find_element(By.NAME, 'username')
        username.send_keys("TestUser1")

        pwd = driver.find_element(By.NAME, 'password')
        pwd.send_keys("12345")

        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div/div[1]/div/div/form/div/button"
        ).click()

        time.sleep(1)

        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/"
        )

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

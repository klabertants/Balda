from selenium.webdriver import Safari
import unittest
import time
from selenium.webdriver.common.by import By

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = Safari()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(2048, 1280)

    def test_registration(self):
        driver = self.driver

        driver.get('http://127.0.0.1:8000/register/')

        username = driver.find_element(By.NAME, 'username')
        username.send_keys("TestUser1")

        fname = driver.find_element(By.NAME, 'first_name')
        fname.send_keys("Fname")

        lname = driver.find_element(By.NAME, 'last_name')
        lname.send_keys("Lname")

        pwd1 = driver.find_element(By.NAME, 'password1')
        pwd1.send_keys("12345")

        pwd2 = driver.find_element(By.NAME, 'password2')
        pwd2.send_keys("12345")

        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/form/div[2]/div/input"
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

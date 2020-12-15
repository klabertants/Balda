from selenium.webdriver import Safari
import unittest
import time
from selenium.webdriver.common.by import By

class OnePlayerPlay(unittest.TestCase):

    def setUp(self):
        self.driver = Safari()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(2048, 1280)

        self.driver.get('http://127.0.0.1:8000/login/')

        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys("TestUser1")

        pwd = self.driver.find_element(By.NAME, 'password')
        pwd.send_keys("12345")

        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div/div[1]/div/div/form/div/button"
        ).click()

        time.sleep(1)

    def test_one_player_cant_play(self):
        driver = self.driver

        driver.get('http://127.0.0.1:8000/')

        driver.find_element(
            By.XPATH,
            "/html/body/nav/div/div/ul[1]/li/a"
        ).click()

        time.sleep(1)

        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/game_wait/"
        )

        time.sleep(10)

        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/game_wait/"
        )

    def test_one_player_can_play_with_bot(self):
        driver = self.driver

        driver.get('http://127.0.0.1:8000/')

        driver.find_element(
            By.XPATH,
            "/html/body/nav/div/div/ul[1]/li/a"
        ).click()

        time.sleep(1)

        self.assertEqual(
            driver.current_url,
            "http://127.0.0.1:8000/game_wait/"
        )

        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div/div[1]/div/button[2]"
        ).click()

        time.sleep(1)

        self.assertTrue(
            "/game/" in driver.current_url
        )



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

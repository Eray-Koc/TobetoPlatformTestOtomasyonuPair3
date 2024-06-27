from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class ScreenShotClass:
    def __init__(self, driver):
        self.driver = driver

    def screenShot(self,screnshotName):
        screenshot_dir = "./screenshots"
        if  not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"ss_{screnshotName}.png")
        self.driver.save_screenshot(screenshot_path)
import pytest
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test_CalendarFunctionality :
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()

    def openCalendarPage(self):
        calendar_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".calendar-btn"))
        ).click()

    def selectedCheckBox(self):
        filters = ["eventEnded", "eventContinue", "eventBuyed", "eventNotStarted"]
        for filter_name in filters:
            filter_checkbox = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.NAME, filter_name))
            ).click()
            sleep(3)

    def test_viewingAllEducations(self):
        self.openCalendarPage()
        self.selectedCheckBox()
        
    def test_educationSearchFilter(self):
        self.openCalendarPage()
        self.selectedCheckBox()
        
        search_input = self.driver.find_element(By.ID, "search-event")
        search_input.click() 
        search_input.send_keys("Test")
        sleep(3)

    def test_instructorSearchFilter(self):
        self.openCalendarPage()
        self.selectedCheckBox()

        egitmenDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-19bb58m"))
        ).click()
        egitmenOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-select-2-option-3"))
        ).click()    
        sleep(3)
    
    
    def test_instructorandEducationSearchFilters(self):
        self.openCalendarPage()
        self.selectedCheckBox()

        egitmenDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-19bb58m"))
        ).click()
        egitmenOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-select-2-option-3"))
        ).click()
        search_input = self.driver.find_element(By.ID, "search-event")
        search_input.click() 
        search_input.send_keys("Test")
        sleep(3)
            
    
    def test_ControlofDateGuidanceButtons(self):
        self.openCalendarPage()
        self.selectedCheckBox()
        
        todayButton = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-today-button.fc-button.fc-button-primary"))
        ).click() 
        
        leftButton = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".fc-prev-button.fc-button.fc-button-primary"))
        ).click()
        rightButton = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".fc-next-button.fc-button.fc-button-primary"))
        ).click()
        rightButton.click()
        monthButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".fc-dayGridMonth-button"))
        ).click()
        weekButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".fc-timeGridWeek-button"))
        ).click()
        sleep(3)

    
    def test_closeCalendarPopup(self):
        self.openCalendarPage()
        sleep(3)
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-close-white"))
        ).click()
        

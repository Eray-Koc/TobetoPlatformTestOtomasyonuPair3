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

from publicClass import ScreenShotClass

class Test_CalendarFunctionality :
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.screenshot_helper = ScreenShotClass(self.driver)
        self.vars = {}        
    
    def teardown_method(self, method):
        self.driver.quit()


    def openCalendarPage_decorator(func):
        def openCalendarPage(self):
            calendar_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".calendar-btn"))
            )
            calendar_button.click()
            func(self)

        return openCalendarPage    

    def selectedCheckBox_decorator(func):
        def selectedCheckBox(self):
            filters = ["eventEnded", "eventContinue", "eventBuyed", "eventNotStarted"]
            for filter_name in filters:
                filter_checkbox = WebDriverWait(self.driver,2).until(
                    EC.element_to_be_clickable((By.NAME, filter_name))
                ).click()
            sleep(3)
            func(self)
        return selectedCheckBox    

    @openCalendarPage_decorator 
    @selectedCheckBox_decorator
    def test_viewingAllEducations(self):
        self.screenshot_helper("allEducation_ExpectedResult")
        assert self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/span").text == "Eğitim ve Etkinlik Takvimi"


    @openCalendarPage_decorator 
    @selectedCheckBox_decorator
    def test_educationSearchFilter(self):
        search_input = self.driver.find_element(By.ID, "search-event")
        search_input.click() 
        search_input.send_keys("Test")
        sleep(3)
        self.screenshot_helper("educationSearch_ExpectedResult")
        assert self.driver.find_element(By.XPATH, 
                    "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[1]/td[3]/div/div[2]/div[1]/a/div/span[2]").text == "Yazılım Kalite ve Test Uzmanı - 3A"

    @openCalendarPage_decorator 
    @selectedCheckBox_decorator
    def test_instructorSearchFilter(self):
        instructorDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-19bb58m"))
        )
        instructorDropdown.click()
        instructorOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-select-2-option-9"))
        )
        instructorOption.click()    
        sleep(3)
        self.screenshot_helper("instructorSearch_ExpectedResult")
        assert self.driver.find_element(By.CSS_SELECTOR, 
                                        "tr:nth-child(1) > .fc-day:nth-child(1) .fc-daygrid-event-harness:nth-child(1) .text-truncate:nth-child(3)").text == "Gürkan İlişen"
    
    @openCalendarPage_decorator 
    @selectedCheckBox_decorator
    def test_instructorandEducationSearchFilters(self):
        instructorDropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-19bb58m"))
        )
        instructorDropdown.click()

        instructorOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-select-2-option-9"))
        )
        instructorOption.click()
        self.screenshot_helper("instructorSearchTogether_ExpectedResult")
        assert self.driver.find_element(By.CSS_SELECTOR, 
                                        "tr:nth-child(1) > .fc-day:nth-child(1) .fc-daygrid-event-harness:nth-child(1) .text-truncate:nth-child(3)").text == "Gürkan İlişen"
        search_input = self.driver.find_element(By.ID, "search-event")
        search_input.click() 
        search_input.send_keys("Test")
        self.screenshot_helper("educationSearchTogether_ExpectedResult")
        assert self.driver.find_element(By.XPATH, 
                    "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[1]/td[3]/div/div[2]/div[1]/a/div/span[2]").text == "Yazılım Kalite ve Test Uzmanı - 3A"

        sleep(3)
            
    @openCalendarPage_decorator 
    @selectedCheckBox_decorator
    def test_ControlofDateGuidanceButtons(self):
        
        leftButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-icon-chevron-left"))
        )
        leftButton.click()
        self.screenshot_helper("beforeButton_ExpectedResult")
        assert self.driver.find_element(By.ID, "fc-dom-1").text == "Mayıs 2024"
        
        sleep(5)
        todayButton = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/button"))
        )
        todayButton.click() 
        self.screenshot_helper("todayButton_ExpectedResult")
        assert self.driver.find_element(By.ID, "fc-dom-1").text == "Haziran 2024"

        rightButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-icon-chevron-right"))
        )
        rightButton.click()
        self.screenshot_helper("afterButton_ExpectedResult")
        assert self.driver.find_element(By.ID, "fc-dom-1").text == "Temmuz 2024"
        
        todayButton.click()
        monthButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".fc-dayGridMonth-button"))
        )
        monthButton.click()
        self.screenshot_helper("monthButton_ExpectedResult")
        assert self.driver.find_element(By.ID, "fc-dom-1").text == "Temmuz 2024"
        
        weekButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".fc-timeGridWeek-button"))
        )
        weekButton.click()
        self.screenshot_helper("weekButton_ExpectedResult")
        assert self.driver.find_element(By.ID, "fc-dom-1").text == "24 – 30 Haz 2024"

        dayButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-timeGridDay-button"))
        )
        dayButton.click()
        self.screenshot_helper("dayButton_ExpectedResult")
        assert self.driver.find_element(By.ID, "fc-dom-1").text == "25 Haziran 2024"
        sleep(3)

    @openCalendarPage_decorator 
    def test_closeCalendarPopup(self):
        sleep(3)
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-close-white"))
        )
        close_button.click()
        self.screenshot_helper("closeCalendarButton_ExpectedResult")
        assert self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[2]").text == "Hoşgeldiniz"


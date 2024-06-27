import json
import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from publicClass import ScreenShotClass

class Test_SignUpPanelControl:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.screenshot_helper = ScreenShotClass(self.driver)
        self.actions = ActionChains(self.driver)
        signUpButton = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[3]/button[2]"))
        )
        signUpButton.click()

    def teardown_method(self, method):
        self.driver.quit()

    def newPage_OpenClose(self):
        #Bu fonksiyon açılan yeni pencereyi kapatıp en son açık olan sayfaya geri dönmek için kullanılır
        main_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break

        self.driver.close()
        self.driver.switch_to.window(main_window)

    def inputForSignUp(self,name,surname,mail,password,passwordAgain,phone):
        name_input = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div.icon-input-group input[name='firstName']"))
        )
        name_input.click()
        name_input.send_keys(name)

        surname_input = WebDriverWait(self.driver,2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div.icon-input-group input[name='lastName']"))
            )
        surname_input.click()
        surname_input.send_keys(surname)

        mail_input = WebDriverWait(self.driver,2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div.icon-input-group input[name='email']"))
            )
        mail_input.click()
        mail_input.send_keys(mail)

        password_input = WebDriverWait(self.driver,2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div.icon-input-group input[name='password']"))
            )
        password_input.click()
        password_input.send_keys(password)

        passwordAgain_input = WebDriverWait(self.driver,2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div.icon-input-group input[name='passwordAgain']"))
            )
        passwordAgain_input.click()
        passwordAgain_input.send_keys(passwordAgain)  

        signUpButton = WebDriverWait(self.driver,2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".btn.btn-primary.w-100.mt-4"))
        )
        signUpButton.click()
        sleep(3)

        contractsForSignup_ExpectedResult = self.driver.find_element(By.CSS_SELECTOR,".alert-message.mx-3").text == "Kayıt oluşturmak için gerekli sözleşmeler"
        self.screenshot_helper.screenShot("contractsForSignup_ExpectedResult")
        assert contractsForSignup_ExpectedResult

        personalData = WebDriverWait(self.driver,3).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(., 'Kişisel verileriniz')]"))
        )
        clarificationText = personalData.find_element(By.XPATH, ".//a")
        clarificationText.click()

        self.newPage_OpenClose()

        explicitConsentText = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(., 'Açık Rıza Metni')]"))
        )
        explicitConsentText_Link = explicitConsentText.find_element(By.XPATH, ".//a")
        explicitConsentText_Link.click()
        self.newPage_OpenClose()
        explicitConsentText_checkbox = explicitConsentText.find_element(By.CSS_SELECTOR, "input[name='contact']")
        explicitConsentText_checkbox.click()

        membershipAgreement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[contains(., 'Üyelik Sözleşmesi ve Kullanım Koşulları')]"))
        )
        membershipAgreement_link = membershipAgreement.find_element(By.XPATH, ".//a")
        membershipAgreement_link.click()
        self.newPage_OpenClose()
        membershipAgreement_checkbox = membershipAgreement.find_element(By.CSS_SELECTOR, "input[name='membershipContrat']")
        membershipAgreement_checkbox.click()

        emailConfirmation_chechbox = self.driver.find_element(By.CSS_SELECTOR,"input[name='emailConfirmation']")
        emailConfirmation_chechbox.click()

        phoneConfirmation_chechbox = self.driver.find_element(By.CSS_SELECTOR,"input[name='phoneConfirmation']")
        phoneConfirmation_chechbox.click()

        phoneNumber_input = WebDriverWait(self.driver,2).until(
            EC.element_to_be_clickable((By.ID,"phoneNumber"))
        )
        phoneNumber_input.click()
        phoneNumber_input.send_keys(phone)

        continueButton = WebDriverWait(self.driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='alert-buttons']//button[@class='btn btn-yes my-3']")))
        continueButton.click()
        sleep(5)
        
    def test_successfulSignUp(self):
        name = "Ahmet"
        surname= "Güneş"
        mail = "ahmetGunes@gmail.com"
        password= "1234563"
        passwordAgain ="1234563"
        phone = "05061110099"
        self.inputForSignUp(name,surname,mail,password,passwordAgain,phone)
        succesfulExpectedResult = WebDriverWait(self.driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,".toast-body")))
        #self.screenshot_helper.screenShot("succesSignUp_ExpectedResult")
        assert succesfulExpectedResult.text == "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."

    def test_existingAccount(self):
        name = "Ayşe"
        surname= "Yılmaz"
        mail = "usengeccpandaa@gmail.com"
        password= "123456"
        passwordAgain ="123456"
        phone = "05062202020"
        self.inputForSignUp(name,surname,mail,password,passwordAgain,phone)
        self.screenshot_helper.screenShot("existingAccount_ExpectedResult")
        assert True
    
    def test_phoneNumberControll(self):

        name = "Ayşe"
        surname = "Yılmaz"
        mail = "usengeccpandaa@gmail.com"
        password = "123456"
        passwordAgain = "123456"
        phone_numbers = ["050622020", "050622020646", "","abc"]

        for phone in phone_numbers:
            self.inputForSignUp(name,surname, mail, password, passwordAgain, phone)

        errorMessageForPhone = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) div label:nth-child(4) small p").text
        if phone == "05062202020":
            phoneMessageText = "En az 10 karakter girmelisiniz."
            self.screenshot_helper.screenShot("phoneMessageTextSmall_ExpectedResult")
            assert errorMessageForPhone == phoneMessageText
        elif phone == "050622020646":
            phoneMessageText = "En fazla 10 karakter girebilirsiniz."
            self.screenshot_helper.screenShot("phoneMessageTextLong_ExpectedResult")
            assert errorMessageForPhone == phoneMessageText
        elif phone == "":
            phoneMessageText = "Doldurulması zorunlu alan*"
            self.screenshot_helper.screenShot("phoneMessageTextEmpty_ExpectedResult")
            assert errorMessageForPhone == phoneMessageText
        elif phone == "abc":    
            phoneMessageText = "Doldurulması zorunlu alan*"
            self.screenshot_helper.screenShot("phoneMessageTextABC_ExpectedResult")
            assert errorMessageForPhone == phoneMessageText
    
    def test_smallPasswordControll(self):
        name = "Ayşe"
        surname = "Yılmaz"
        mail = "klm@gmail.com"
        password = "12345"
        passwordAgain ="12345"
        phone = "05062205510"
        self.inputForSignUp(name,surname,mail,password,passwordAgain,phone)
        sleep(1)
        self.screenshot_helper.screenShot("passwordIsSmall_ExpectedResult")
        assert True

    def test_passwordAgainControll(self):
        name = "Ayşe"
        surname = "Yılmaz"
        mail = "usengecpanda@gmail.com"
        password = "123456"
        passwordAgain ="asdf"
        phone = "05062205544"
        self.inputForSignUp(name,surname,mail,password,passwordAgain,phone)
        sleep(1)
        self.screenshot_helper.screenShot("passwordIsNotSame_ExpectedResult")
        assert True

    def test_twoDifferentErrorsControll(self):
        name = "Ayşe"
        surname = "Yılmaz"
        mail = "usengeccpandaa@gmail.com"
        password = "123456"
        passwordAgain ="asdf"
        phone = "05062205544"
        self.inputForSignUp(name,surname,mail,password,passwordAgain,phone)
        sleep(1)
        self.screenshot_helper.screenShot("passwordIsNotSame_ExpectedResult")
        assert True

    def test_invalidMail(self):
        mail_input = WebDriverWait(self.driver,2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div.icon-input-group input[name='email']"))
            )
        mail_input.click()
        mail_input.send_keys("e")
        invalidMailMessage = self.driver.find_element(By.XPATH, "//p[@style='text-align: start; color: red;']").text
        sleep(1)
        self.screenshot_helper.screenShot("invalidMail_ExpectedResult")
        assert invalidMailMessage == "Geçersiz e-posta adresi*"
        
        sleep(2)
        mail_input.clear()
        sleep(2)
        mail_input.click
        mail_input.send_keys("a")
        mail_input.clear
        emptyMailMessage = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p[style='text-align: start; color: red;']:nth-of-type(1)"))
        )
        sleep(1)
        self.screenshot_helper.screenShot("emptyMail_ExpectedResult")
        assert emptyMailMessage == "Doldurulması zorunlu alan*"
        

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class TestSENARYOSU13():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_kisiselbilgileringuncellenmesi(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     self.driver.find_element(By.NAME, "name").send_keys("Eray")
     self.driver.find_element(By.NAME, "surname").send_keys("Koç")
     self.driver.find_element(By.ID, "phoneNumber").send_keys("+902222222222")
     self.driver.find_element(By.NAME, "birthday").send_keys("2003-01-14")
     gender = self.driver.find_element(By.ID, "react-select-2-input")
     gender.send_keys("Erkek")
     gender.send_keys(Keys.ENTER)
     self.driver.find_element(By.XPATH, "//*[@id='react-select-3-input']").send_keys("T", Keys.ENTER)
     self.driver.find_element(By.ID, "react-select-4-input").send_keys("Yok")
     git = self.driver.find_element(By.NAME, "githubAddress")
     git.send_keys(Keys.CONTROL, 'a')
     git.send_keys("www.github.com/Eray-Koc")
     country = self.driver.find_element(By.NAME, "country")
     country.send_keys(Keys.CONTROL, 'a')
     country.send_keys("Türkiye")
     dropdown = self.driver.find_element(By.NAME, "city")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     dropdown = self.driver.find_element(By.NAME, "district")
     dropdown.find_element(By.XPATH, "//option[. = 'Avcılar']").click()
     street = self.driver.find_element(By.NAME, "address")
     street.send_keys(Keys.CONTROL, 'a')
     street.send_keys("Yenimahalle mh.")
     about = self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(16) > .form-control")
     about.send_keys(Keys.CONTROL, 'a')
     about.send_keys("Tobeto Yazılım Test Mühendisi")
     sleep(5)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Bilgileriniz başarıyla güncellendi."

  @succesful_login_decorator
  def test_profilresmieklekontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     self.driver.find_element(By.CSS_SELECTOR, ".photo-edit-btn").click()
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input[1]").send_keys(r"C:\Users\kocer\OneDrive\Desktop\vscodepng.png")
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button").click()
     try:
         self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div[2]")
         assert True
     except:
         assert False

  @succesful_login_decorator
  def test_TCKN11HanedenFazlaKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     self.driver.find_element(By.NAME, "identifier").send_keys("491382227867")
     value = self.driver.find_element(By.NAME, "identifier").get_attribute("value")
     assert value == "49138222786"
  
  @succesful_login_decorator
  def test_TCKNBosBirakmaKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     tckn = self.driver.find_element(By.NAME, "identifier")
     tckn.send_keys(Keys.CONTROL, 'a')
     tckn.send_keys(Keys.BACK_SPACE)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()
     assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span").text == "Satın alınan eğitimlerin faturası için doldurulması zorunlu alan."
  
  @succesful_login_decorator
  def test_MahalleKarakterKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     sleep(4)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[15]/textarea").send_keys("askdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnasasasass")
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[15]/span[1]")))
     assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[15]/span[1]").text == "En fazla 200 karakter girebilirsiniz"

  @succesful_login_decorator
  def test_HakkindaKarakterKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     sleep(4)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[16]/textarea").send_keys("askdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnasasasassaaskdjasndkjnaskjdnakjsdaskdjasndkjnaskjdnakjsdaskdjasndkjnaskjdnakjsdaskdjasndkjnaskjdnakjsdaskdjax")
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[16]/span[1]")))
     assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[16]/span[1]").text == "En fazla 300 karakter girebilirsiniz"
class TestSENARYOSU14():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_BasariliDeneyimEklemesi(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("TOBETO")
     self.driver.find_element(By.NAME, "position").send_keys("YAZILIM TEST")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("YAZILIM")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("TOBETO")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Deneyim eklendi."

  @succesful_login_decorator
  def test_IsAciklamasiKarakterKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("TOBETO")
     self.driver.find_element(By.NAME, "position").send_keys("YAZILIM TEST")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("YAZILIM")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("buraonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfq")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[8]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[8]/span").text == "En fazla 300 karakter girebilirsiniz"

  @succesful_login_decorator
  def test_KurumSektorEnAzKarakterKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("YAZI")
     self.driver.find_element(By.NAME, "position").send_keys("YAZILIM TEST")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("YAZI")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("TOBETO")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span").text == "En az 5 karakter girmelisiniz"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[4]/span").text == "En az 5 karakter girmelisiniz"

  @succesful_login_decorator
  def test_KurumSektorPozisyonEnFazlaKarakterKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("TOBEjcsnscajsjcnajcsnasjcnajsnasjnckasjcnajkcnajkcnj")
     self.driver.find_element(By.NAME, "position").send_keys("TOBEjcsnscajsjcnajcsnasjcnajsnasjnckasjcnajkcnajkcnj")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("TOBEjcsnscajsjcnajcsnasjcnajsnasjnckasjcnajkcnajkcnj")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("TOBETO")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span").text == "En fazla 50 karakter girebilirsiniz"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[2]/span").text == "En fazla 50 karakter girebilirsiniz"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[4]/span").text == "En fazla 50 karakter girebilirsiniz"

  @succesful_login_decorator
  def test_KurumSektorPozisyonBosBirakilmaKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span").text == "Doldurulması zorunlu alan*"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[2]/span").text == "Doldurulması zorunlu alan*"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[4]/span").text == "Doldurulması zorunlu alan*"

class TestSENARYOSU15():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_BasariliEgitimEkleme(self):
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
    self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[3]/span[2]")))
    self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[3]/span[2]").click()
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select__input-container")))
    sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
    self.driver.find_element(By.ID, "react-select-5-option-2").click()
    self.driver.find_element(By.NAME, "University").send_keys("Erzincan Üniversitesi")
    self.driver.find_element(By.NAME, "Department").send_keys("Yazılım")
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(4) .form-control").send_keys("2020")
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(5) .form-control").send_keys("2024")
    self.driver.find_element(By.NAME, "Department").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Eğitim bilgisi eklendi."

class TestSENARYOSU16():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_BasariliYetkinlikEklenmesi(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-19bb58m")))
     self.driver.find_element(By.CSS_SELECTOR, ".css-19bb58m").click()
     self.driver.find_element(By.ID, "react-select-5-option-1").click()
     sleep(2)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Yetenek eklendi."


  @succesful_login_decorator
  def test_BosBirakilanYetkinlikKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(5)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Herhangi bir yetenek seçmediniz!"

  @succesful_login_decorator
  def test_SecillenYetkinliginSilinmesiKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/div[1]/div/button")))
     sleep(4)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-yes")))
     self.driver.find_element(By.CSS_SELECTOR, ".btn-yes").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Yetenek kaldırıldı."


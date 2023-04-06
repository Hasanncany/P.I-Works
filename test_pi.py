from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from datetime import date
import pytest
from time import sleep

class Test_PI_Works():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://piworks.net/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(locator))

    # Learn More butonuna tıklama
    def test_learn_more(self):
        self.wait_for_element_visible((By.XPATH, "//*[@id='get5gready']/div/div/div[2]/span/a[1]"))
        learn_more_button = self.driver.find_element(By.XPATH, "//*[@id='get5gready']/div/div/div[2]/span/a[1]")
        learn_more_button.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-Learn-More.png")

    #Talk To Us butonu
    def test_talk_to_us(self):
        self.wait_for_element_visible((By.XPATH, "//*[@id='get5gready']/div/div/div[2]/span/a[2]"))
        talk_to_us_button = self.driver.find_element(By.XPATH,"//*[@id='get5gready']/div/div/div[2]/span/a[2]")
        talk_to_us_button.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-Talk-To-Us.png")

        

    # About butonu
    def test_about(self):
        self.wait_for_element_visible((By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[3]/a"))
        aboutBtn = self.driver.find_element(By.XPATH,"//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[3]/a")
        aboutBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-About.png")
        

    #Search Button
    @pytest.mark.parametrize("text",[("services")])
    def test_search(self,text):
        self.wait_for_element_visible((By.XPATH, "(//input[@id=\'search\'])[2]"))
        searchBtn = self.driver.find_element(By.XPATH, "(//input[@id=\'search\'])[2]")
        searchBtn.click()

        action = ActionChains(self.driver)
        action.send_keys_to_element(searchBtn,text)
        action.perform()
        self.driver.save_screenshot(f"{self.folderPath}/test-Search.png")
        
        enter = self.driver.find_element(By.XPATH, "(//input[@id=\'search\'])[2]")
        enter.send_keys(Keys.ENTER)
        sleep(5)
        self.driver.save_screenshot(f"{self.folderPath}/test-Searching.png")

    #Careers Butonu
    def test_careers(self):
        self.wait_for_element_visible((By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[4]/a"))
        careersBtn = self.driver.find_element(By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[4]/a")
        careersBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-careers.png")
        

    #Insights butonu
    def test_insights(self):
        self.wait_for_element_visible((By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[2]/a"))
        insightsBtn = self.driver.find_element(By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[2]/a")
        insightsBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-Insights.png")


    #Offerings butonu
    def test_offerings(self):
        self.wait_for_element_visible((By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[1]/a"))
        offeringsBtn = self.driver.find_element(By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/ul/li[1]/a")
        offeringsBtn.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Offerings.png")


    #Contact us bilgileri girme
    @pytest.mark.parametrize("name,surname,email,company,job,phone,message",[("Hasancan","Yıldırım","abc@hotmail.com","Company Name","CE","12345","Hello")])
    def test_contact_us(self,name,surname,email,company,job,phone,message):
        self.wait_for_element_visible((By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/a[2]"))
        contact_us_button = self.driver.find_element(By.XPATH, "//*[@id='root']/header/div/div/div/nav/div[4]/a[2]")
        contact_us_button.click()
        
        #Çerezleri kapama
        self.wait_for_element_visible((By.XPATH, "//*[@id='cookiediv']/div/button/b[1]"))
        cookieDiv = self.driver.find_element(By.XPATH,"//*[@id='cookiediv']/div/button/b[1]")
        cookieDiv.click()

        self.wait_for_element_visible((By.XPATH, "//*[@id='contact']/div/div[1]/div/input"))
        nameInput = self.driver.find_element(By.XPATH, "//*[@id='contact']/div/div[1]/div/input")

        self.wait_for_element_visible((By.XPATH, "//*[@id='contact']/div/div[2]/div/input"))
        surnameInput = self.driver.find_element(By.XPATH, "//*[@id='contact']/div/div[2]/div/input")

        self.wait_for_element_visible((By.XPATH,"//*[@id='contact']/div/div[3]/div/input"))
        emailInput = self.driver.find_element(By.XPATH,"//*[@id='contact']/div/div[3]/div/input")

        self.wait_for_element_visible((By.XPATH, "//*[@id='contact']/div/div[4]/div/input"))
        companyInput = self.driver.find_element(By.XPATH, "//*[@id='contact']/div/div[4]/div/input")

        self.wait_for_element_visible((By.XPATH, "//*[@id='contact']/div/div[5]/div/input"))
        jobInput = self.driver.find_element(By.XPATH, "//*[@id='contact']/div/div[5]/div/input")

        self.wait_for_element_visible((By.XPATH, "//*[@id='contact']/div/div[6]/div/input"))
        phoneInput = self.driver.find_element(By.XPATH, "//*[@id='contact']/div/div[6]/div/input")

        self.wait_for_element_visible((By.XPATH, "//*[@id='contact']/div/div[8]/div/textarea"))
        messageInput = self.driver.find_element(By.XPATH,"//*[@id='contact']/div/div[8]/div/textarea")

        action = ActionChains(self.driver)
        action.send_keys_to_element(nameInput,name)
        action.send_keys_to_element(surnameInput,surname)
        action.send_keys_to_element(emailInput,email)
        action.send_keys_to_element(companyInput,company)
        action.send_keys_to_element(jobInput,job)
        action.send_keys_to_element(phoneInput,phone)
        action.send_keys_to_element(messageInput,message)
        action.perform()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Contact-Us-Entering-Information.png")


        self.wait_for_element_visible((By.XPATH, "//*[@id='contact']/div/div[7]/div/select"))
        categoryInput = self.driver.find_element(By.XPATH, "//*[@id='contact']/div/div[7]/div/select")
        categoryInput.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Contact-Us-Select-Category.png")



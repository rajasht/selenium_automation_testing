import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# from webdriver_manager.chrome import ChromeDriverManager
class snowmobile():
    def __init__(self):
        self.options = Options()
        self.options = webdriver.ChromeOptions()
        self.chromepath = r"/home/shtlp0064/selenium_chrome/drivers/chromedriver"
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.options, executable_path=self.chromepath)

    def execute(self):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.execute_cdp_cmd("Network.setUserAgentOverride", {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.get("https://qa.dev.snowmobiletrader.com/listing/2019-Yamaha-HYDRA-5015433697")

        self.timeLap()
        self.openMAOForm()

        # open MAO/BYD form

    def openMAOForm(self):
        # self.driver.find_element(By.XPATH,
        #                        "//*[@class='optanon-alert-box-button-middle accept-cookie-container']").click()
        self.driver.find_element(By.XPATH, "//*[@id='offer-buttons']/a").click()
        self.timeLap()
        self.fillMAOForm()

    # //*[@id='listing_info_5015433697']/a/div[2]/div[1]/span/button
    # fill MAO/BYD form

    def fillMAOForm(self):
        self.fillContactInfo()
        self.openTradeInForm()
        self.openReviewPaymentOption()
        self.openMessageDealer()
        self.submit()

        # submit MAO form

    def submit(self):
        self.driver.find_element(By.XPATH, "//*[@id='submit-offer-button']").click()

    # sleep time after a work perform
    def timeLap(self):
        time.sleep(5)

    # offer amount
    def fillOfferAmount(self):
        offer = self.driver.find_element(By.XPATH, "//*[@id='input-field-offer']")
        offer.click()
        offer.send_keys("8000000")

    # phone number
    def fillPhoneNumber(self):
        phonenumber = self.driver.find_element(By.XPATH, "//*[@id='input-field-phone-number']")
        phonenumber.click()
        phonenumber.send_keys("8769875667")

    # email
    def fillEmail(self):
        email = self.driver.find_element(By.XPATH, "//*[@id='input-field-email']")
        email.click()
        email.send_keys("tradertestmail@gmail.com")

    # last name
    def fillLastName(self):
        lastname = self.driver.find_element(By.XPATH, "//*[@id='input-field-last-name']")
        lastname.click()
        lastname.send_keys("Singh")

    # first Name
    def fillFirstName(self):
        firstname = self.driver.find_element(By.XPATH, "//*[@id='input-field-first-name']")
        firstname.click()
        firstname.send_keys("Abhay")

    # year
    def fillYear(self):
        year = self.driver.find_element(By.XPATH, "//*[@id='vs1__combobox']/div[1]/input")
        year.click()
        year.send_keys(Keys.ARROW_DOWN * 6, Keys.ENTER)
        self.timeLap()

    # make
    def fillMake(self):
        make = self.driver.find_element(By.XPATH, "//*[@id='input-field-make']")
        make.click()
        make.send_keys("hero")

    # modal
    def fillModal(self):
        modal = self.driver.find_element(By.XPATH, "//*[@id='input-field-model']")
        modal.click()
        modal.send_keys("honda")

    # estimatedmileage
    def fillestimatedmileage(self):
        estimatedmileage = self.driver.find_element(By.XPATH, "//*[@id='input-field-mileage']")
        estimatedmileage.click()
        estimatedmileage.send_keys("5876")

    # vin
    def fillVIN(self):
        vin = self.driver.find_element(By.XPATH, "//*[@id='input-field-vin']")
        vin.click()
        vin.send_keys("58768989765432134")

    # fill trade in form
    def fillTradeInForm(self):
        self.fillYear()
        self.fillMake()
        self.fillModal()
        self.fillestimatedmileage()
        self.fillVIN()

    # open tradeIn form
    def openTradeInForm(self):
        tradein = self.driver.find_element(By.XPATH, "//*[@id='ti-with-accordion']/div[2]/div/p/b")
        tradein.click()
        self.timeLap()
        self.fillTradeInForm()

    # fill Contact information of user
    def fillContactInfo(self):
        self.fillFirstName()
        self.fillLastName()
        self.fillEmail()
        self.fillPhoneNumber()
        self.fillOfferAmount()

    # credit
    def fillCredit(self):
        credit = self.driver.find_element(By.XPATH, "//*[@id='vs7__combobox']/div[1]/input")
        credit.send_keys(Keys.ARROW_DOWN * 2, Keys.ENTER)

    # finance
    def fillFinance(self):
        finance = self.driver.find_element(By.XPATH,
                                           "//*[@id='payment-with-accordion']/div[3]/div/div[3]/div/span[1]/label")
        finance.click()
        self.timeLap()
        self.fillCredit()

    # cash
    def fillCash(self):
        cash = self.driver.find_element(By.XPATH, "//*[@id='payment-with-accordion']/div[3]/div/div[2]/div")
        cash.click()
        self.timeLap()

    # review payment form
    def fillReviewpayment(self):
        # change the value of payment type to check cash or financing
        paymentType = "cash"
        if paymentType == "cash":
            self.fillCash()
        else:
            self.fillFinance()

    # review payment option
    def openReviewPaymentOption(self):
        payment = self.driver.find_element(By.XPATH, "//*[@id='payment-with-accordion']/div[2]/div/p/b")
        payment.click()
        self.timeLap()
        self.fillReviewpayment()

    # message to dealer
    def messageToDealer(self):
        messagetext = self.driver.find_element(By.XPATH,
                                               "//*[@id='message-with-accordion']/div[3]/div/div[1]/div/div/textarea")
        messagetext.send_keys("testing")

    # open Message to dealer
    def openMessageDealer(self):
        message = self.driver.find_element(By.XPATH, "//*[@id='message-with-accordion']/div[2]")
        message.click()
        self.timeLap()
        self.messageToDealer()


if __name__ == '__main__':
    objesnowmobile = snowmobile()
    objesnowmobile.execute()

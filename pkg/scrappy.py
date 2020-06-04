from selenium import webdriver
from time import sleep



class SDscraper:
    def __init__(self, benutzername, pw):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        self.id = id
        self.benutzername = benutzername
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Anmelden')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"E-Mail\"]")\
            .send_keys(benutzername)
        self.driver.find_element_by_xpath("//input[@name=\"Passwort\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="Anmelden"]') \
            .click()
        sleep(4)

    def print_shit(self):
        print("hi")



if __name__ == "__main__":
    sds = SDscraper("antonthielmann@t-online.de", "passwd")
    sds.print_shit()
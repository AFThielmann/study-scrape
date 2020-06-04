import json
from time import sleep
from webbot import Browser
from bs4 import BeautifulSoup


class SDscraper:
    def __init__(self):
        self.web = Browser()
        self.web.go_to("https://www.studydrive.net/de")
        self.web.click('Anmelden')
        sleep(2)

    def login(self):
        with open("login.json", "r") as lg:
            LG = json.load(lg)
        self.benutzername = LG['email']
        self.pw = LG['password']
        self.web.type(self.benutzername, into="E-Mail")
        self.web.type(self.pw, into="Passwort")
        sleep(2)

        self.web.click('Anmelden')


    def go_to_course(self):
        self.web.click("Mathematik")
        sleep(5)

    def scrape(self):
        page = self.web.get_page_source()
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.get_text())


if __name__ == "__main__":
    sds = SDscraper()
    sds.login()
    sds.go_to_course()
    sds.scrape()

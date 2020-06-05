import json
from time import sleep
from webbot import Browser
from bs4 import BeautifulSoup
import pandas as pd
import re

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
        soup = BeautifulSoup(page, 'html')
        #print(soup.get_text())
        tags = soup.find_all('div', {"class":"text-area-read"})
        names = soup.find_all('div', {"class":"user-name"})
        text = []
        poster = []
        for t in tags:
            text.append(t.text)
        for k in names:
            poster.append(k.text)

        self.data = {"text": text,
                "poster" : poster}



    def data_cleaning(self):

        self.data = pd.DataFrame(self.data)
        self.data = self.data.replace(r'\n',  ' ', regex=True)

        self.data['text'] = [re.sub(' +', ' ', x) for x in self.data['text']]
        self.data['poster'] = [re.sub(' +', ' ', x) for x in self.data['poster']]

        print(self.data.head(20))
        print(self.data['poster'].head(4))



if __name__ == "__main__":
    sds = SDscraper()
    sds.login()
    sds.go_to_course()
    sds.scrape()
    sds.data_cleaning()

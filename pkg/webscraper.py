import json
import webbot
import time
import bs4


class WebScraper:
    def __init__(self):
        self.url = "https://www.studydrive.net/de"
        self.web = webbot.Browser()
        self.delay = 3
    
    def login(self, lg):
        self.web.go_to(self.url)
        self.web.click('Anmelden')
        time.sleep(self.delay)
        self.web.type(lg['email'], into='E-Mail')
        time.sleep(self.delay)
        self.web.type(lg['password'], into='Passwort')
        time.sleep(self.delay)
        self.web.click('Anmelden')

    def go_to_course(self, course):
        time.sleep(self.delay)
        self.web.click(course)

    def scrape(self):
        time.sleep(self.delay)
        page = self.web.get_page_source()
        soup = bs4.BeautifulSoup(page)
        return soup
        

if __name__ == "__main__":
    ws = WebScraper()
    with open("login.json", "r") as lg:
        LG = json.load(lg)
    ws.login(lg=LG)
    KURSE = ['Informatik', 'Mathematik']
    for kurs in KURSE:
        ws.go_to_course(course = kurs)
        text = ws.scrape()
        print(text)



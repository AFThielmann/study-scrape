import json
import pandas as pd
import webbot
import time
import bs4


class WebScraper:
    """
    WebScraper
    """
    def __init__(self):
        self.url = "https://www.studydrive.net/de"
        self.web = webbot.Browser()
        self.delay = 1
    
    def login(self, lg):
        self.web.go_to(self.url)
        self.web.click('Anmelden')
        time.sleep(self.delay)
        self.web.type(lg['email'], into = 'E-Mail')
        time.sleep(self.delay)
        self.web.type(lg['password'], into = 'Passwort')
        time.sleep(self.delay)
        self.web.click('Anmelden')

    def go_to_course(self, course):
        time.sleep(self.delay)
        self.web.click(course)

    def scrape(self):
        time.sleep(self.delay)
        page = self.web.get_page_source()
        soup = bs4.BeautifulSoup(page)
        texts = soup.find_all('div', {'class' : 'text-area-read'})
        users = soup.find_all('div', {'class' : 'user-name'})
        df_list = []
        qc_key_words = ['Minuten', 'Stunden', 'Wochen', 'Monaten']
        for t, u in zip(texts, users):
            text = t.text.strip()
            text = text.replace('\n', ' ')
            user = u.text.strip()
            qc_type = 'C' if any(w in user for w in qc_key_words) else 'Q'
            user = user.split('\n')[0].strip()
            df_dict = {'text' : text, 'user' : user, 'type' : qc_type}
            df_list.append(df_dict) 
        return pd.DataFrame(df_list)
        

if __name__ == "__main__":
    ws = WebScraper()
    with open("login.json", "r") as lg:
        LG = json.load(lg)
    ws.login(lg = LG)
    ws.go_to_course(course = 'Mathematik')
    df = ws.scrape()
    # df.to_csv('test.csv')
    # print(df)


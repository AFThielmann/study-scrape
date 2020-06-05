import json
from pkg import WebScraper

ws = WebScraper()
with open("login.json", "r") as lg:
    LG = json.load(lg)
ws.login(lg = LG)

KURSE = ['Mathematik']

df_list = []
for kurs in KURSE:
    ws.go_to_course(course = kurs)
    df = ws.scrape()
    print(df)
    df.to_csv('test.csv')
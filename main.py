import json
from pkg import WebScraper
import pandas as pd

ws = WebScraper()
with open("login.json", "r") as lg:
    LG = json.load(lg)
ws.login(lg = LG)

# z.B.
KURSE = ['Multivariate Time Series Analysis', 
         'Ökonometrie I/ Econometrics I',
         'Lineare Modelle',
         'Informatik',
         'Differenzial- und Integralrechnung II',
         'Differential- und Integralrechnung I',
         'Analytische Geometrie und Lineare Algebra II',
         'Mathematik']

df_list = []
for kurs in KURSE:
    ws.go_to_course(course = kurs)
    df = ws.scrape()
    df['course'] = kurs
    df_list.append(df)

df = pd.concat(df_list)
df.to_csv('df.csv')

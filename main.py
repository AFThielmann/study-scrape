import json
from pkg import WebScraper, EmailSender
import pandas as pd


def send_email(temperature):
    fromaddr = "a.f.fertig@gmail.com"
    toaddr = "afthielmann1@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alert: Server Room  "
    body = "Server room current temprature is : " + temperature
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "ffvol28g")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

ws = WebScraper()
es = EmailSender()
with open("pkg/login.json", "r") as lg:
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


# words to filter by, all lowercase
word_list = ["mathe", "eco", "herleitung", "ableitung"]

df = pd.concat(df_list)

# everything lowercase in text
df['text'] = df['text'].str.lower()

df = df[df['text'].apply(lambda x: any([k in x for k in word_list]))]

df = df.reset_index(drop=True)

df_old = pd.read_csv('df.csv')





if df.equals(df_old)==False:
    print('there is new content')

    df_both = pd.concat([df, df_old])
    df_both = df_both.reset_index(drop=True)
    df_gpby = df_both.groupby(list(df_both.columns))
    idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
    df_new = df_both.reindex(idx)

    es.send(" " + str(df_new["course"].unique()))
    df.to_csv('df.csv', index=False)

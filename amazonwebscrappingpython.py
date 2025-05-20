from bs4 import BeautifulSoup
import requests 
import smtplib
import time 
import datetime 

# connect to bebsite 

URL= 'https://www.amazon.com/MSI-Codex-Gaming-Desktop-A8NUE-274US/dp/B0DGHPPL1M/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.860dbf94-9f09-4ada-8615-32eb5ada253a&dib=eyJ2IjoiMSJ9.VF6cimqcEbaH4-ctBeYEEQO7iyC8tXaoTDiLbl62tOYVd9cmzXZdPzTFhFsroJ4HbbooCJSrPz_VzFshhe8Is4-n7SeMH9FwdqumjO2mNt0tCql_r-9O0YuNyuqfc4xVMVT-i1kCghvUAOI2qmta1xH6SATDABGC5rpy1SMgqkhq_1JzdPAVULoMIjfA1V5ZpL7DHuQtFmxTjVXQD3P1xWfhT-8CSDJaceG0dJq8IXc5vUjo73h73nVT3nPkYROEGI-UX5KSs7kwilMGTjaLnTj14jpC9E0lwRsVTRV3qjP22hRcKdMEquNjOQo-43tiRG3eNbpd9Han6rLSv2RbDkQBrOmjgMy8PQbJL6hkIz2-WWW2i5o1iG-FYejqNb0xFe2YyxlEaKpNf8X1IeV45zgJJCxgwk58b-W8Phj18WX89B4IM7VNtOKdihbxaNxp.xdxLSa5N4sU9nTeqbmI9s-mPeGsjjvFjbSQ3897a1jE&dib_tag=se&keywords=gaming&pd_rd_r=7d6d1950-833f-4dd0-a2f3-f119cbc39891&pd_rd_w=yYavN&pd_rd_wg=SQeWx&qid=1742940200&sr=8-2&th=1'

headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x640 AppleWebkit/537.36 (KTML, like Gecko) Chrome/92.0.4515.31 Safari/537.36", "Accept-Encoding": "gzip,deflate","Accept": "text/html, application/xhtml+xml, application/xml;q=0.8","DNT": "1","Connection":"close","Upgerade-Requests":"1"}

page=requests.get(URL, headers=headers)

Soup1= BeautifulSoup(page.content, "html.parser")
print(Soup1)

title=Soup1.find(id="productTitle").get_text()
print(title)

price=Soup1.find(id="corePriceDisplay_desktop_feature_div").get_text()

print(title)
print(price)

price=price.strip()[1:9]
print(price)

import datetime

today= datetime.date.today()

print(today)

import csv

header=["title", "price","date"]
data=[title,price,today]

type(data)

with open("Amazondatascrapping.csv","w", newline="", encoding="UTF8") as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

#append data to csv 


with open("Amazondatascrapping.csv","a+", newline="", encoding="UTF8") as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

def check_price():
    URL= 'https://www.amazon.com/MSI-Codex-Gaming-Desktop-A8NUE-274US/dp/B0DGHPPL1M/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.860dbf94-9f09-4ada-8615-32eb5ada253a&dib=eyJ2IjoiMSJ9.VF6cimqcEbaH4-ctBeYEEQO7iyC8tXaoTDiLbl62tOYVd9cmzXZdPzTFhFsroJ4HbbooCJSrPz_VzFshhe8Is4-n7SeMH9FwdqumjO2mNt0tCql_r-9O0YuNyuqfc4xVMVT-i1kCghvUAOI2qmta1xH6SATDABGC5rpy1SMgqkhq_1JzdPAVULoMIjfA1V5ZpL7DHuQtFmxTjVXQD3P1xWfhT-8CSDJaceG0dJq8IXc5vUjo73h73nVT3nPkYROEGI-UX5KSs7kwilMGTjaLnTj14jpC9E0lwRsVTRV3qjP22hRcKdMEquNjOQo-43tiRG3eNbpd9Han6rLSv2RbDkQBrOmjgMy8PQbJL6hkIz2-WWW2i5o1iG-FYejqNb0xFe2YyxlEaKpNf8X1IeV45zgJJCxgwk58b-W8Phj18WX89B4IM7VNtOKdihbxaNxp.xdxLSa5N4sU9nTeqbmI9s-mPeGsjjvFjbSQ3897a1jE&dib_tag=se&keywords=gaming&pd_rd_r=7d6d1950-833f-4dd0-a2f3-f119cbc39891&pd_rd_w=yYavN&pd_rd_wg=SQeWx&qid=1742940200&sr=8-2&th=1'
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x640 AppleWebkit/537.36 (KTML, like Gecko) Chrome/92.0.4515.31 Safari/537.36", "Accept-Encoding": "gzip,deflate","Accept": "text/html, application/xhtml+xml, application/xml;q=0.8","DNT": "1","Connection":"close","Upgerade-Requests":"1"}
    page=requests.get(URL, headers=headers)
    title=Soup1.find(id="productTitle").get_text()
    price=Soup1.find(id="corePriceDisplay_desktop_feature_div").get_text()
    price=price.strip()[1:9]
    today= datetime.date.today()
    import csv

    header=["title", "price","date"]
    data=[title,price,today]
    with open("Amazondatascrapping.csv","a+", newline="", encoding="UTF8") as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

    if price<= 1500
        send_mail()

def send_email():
    server= smtlib.SMTP.SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('vferentinos1992ab@gmail.com','xxxxxxxxxxx')
    subject='time to buy this pc'
    body='this pc cost lower than 1500$ now, run'

    msg=f"Subject: {subject}\n\n{body}"
    server.sendemail('vferentinos1992ab@gmail.com',msg)

while(True):
    check_price()
    time.sleep(5)

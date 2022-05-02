import requests
from bs4 import BeautifulSoup
import smtplib

# Features about Authorization.
headers = {
            "Accept-Language": "el-GR,el;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/97.0.4692.71 Safari/537.36",
}


response = requests.get("https://www.amazon.com/ILIFE-Pro-ElectroWall-Self-Charging-Tangle-Free/dp/B085VR2WYR/ref=sr_1_"
                        "1_sspa?crid=3FHLBBH3997JR&keywords=Robotic%2BVacuum%2BCleaner&nav_sdd=aps&qid=1642067646&"
                        "sprefix=vac&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFOQVY1MjQ2OTFaVlEmZW5jcnlwdGVkSWQ9QT"
                        "A0Mjc4MThLV0Q1Uk9aOEo3QVkmZW5jcnlwdGVkQWRJZD1BMDgwMDc5ODM5OTJRWURGODRJN0kmd2lkZ2V0TmFtZT1zcF9"
                        "hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1",
                        headers=headers)

html_amazonpage = response.text
soup = BeautifulSoup(html_amazonpage, "lxml")
vacuum_price = float(soup.find(name="span", class_="a-price-whole").text.split(".")[0])

# Infos about email.
SERVER = "smtp.gmail.com"
FROM = "FIRST_EMAIL"
TO = "SECOND_EMAIL"
SUBJECT = "Track the price of vacuum"

msg = 'To:' + TO + '\n' + 'From: ' + FROM + '\n' + f"Subject:{SUBJECT}" + '\n'

TEXT = msg + f"Hurry up!\n The price decreases. Now is {vacuum_price}!"

# Procedure about sending.
if vacuum_price < 100:
    server = smtplib.SMTP(SERVER, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM, "FIRST_EMAIL_PASSWORD")
    server.sendmail(FROM, TO, TEXT)
    server.quit()

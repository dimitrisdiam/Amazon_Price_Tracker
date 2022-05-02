import requests
from bs4 import BeautifulSoup
import smtplib

# Features about Authorization.
headers = {
            "Accept-Language": "en,el;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/101.0.4951.41 Safari/537.36",
}

response = requests.get("https://www.amazon.com/ILIFE-Pro-ElectroWall-Self-Charging-Tangle-Free/dp/B085VR2WYR?ref_=ast_sto_dp&th=1&psc=1_",
                        headers=headers)

html_amazonpage = response.text
soup = BeautifulSoup(html_amazonpage, "lxml")
vacuum_price = float(soup.find(name="span", class_="a-offscreen").text.replace("$",""))

# Infos about email.
SERVER = "smtp.gmail.com"
FROM = "FIRST_EMAIL"
TO = "SECOND_EMAIL"
SUBJECT = "Track the price of vacuum"

msg = 'To:' + TO + '\n' + 'From: ' + FROM + '\n' + f"Subject:{SUBJECT}" + '\n'
TEXT = msg + f"Hurry up!\n The price decreases. Now is {vacuum_price}!"

# Procedure about sending.
if vacuum_price < 200:
    server = smtplib.SMTP(SERVER, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM, "FIRST_EMAIL_PASSWORD")
    server.sendmail(FROM, TO, TEXT)
    server.quit()


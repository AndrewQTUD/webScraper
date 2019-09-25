import requests
from bs4 import BeautifulSoup
import smtplib



URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?crid=35202L8Q4OI7H&keywords=sony+alpha+7m3&qid=1569417505&s=gateway&sprefix=sony+alpha+7m%2Caps%2C206&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()
    

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()



    print(converted_price)
    print(title.strip())

    if(converted_price > 1.700):
        send_mail()




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('andysempai12@gmail.com', 'ocbhdmemnkvkvzea')

    subject = 'Price has decreased.'
    body = 'Check the amazon listing : https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?crid=35202L8Q4OI7H&keywords=sony+alpha+7m3&qid=1569417505&s=gateway&sprefix=sony+alpha+7m%2Caps%2C206&sr=8-3'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'andysempai12@gmail.com',
        'andytown@live.ie',
        msg
    )
    print("The e-mail has been sent")

    server.quit()


check_price()
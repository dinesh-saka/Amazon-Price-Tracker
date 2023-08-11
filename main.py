import requests
import smtplib
import lxml
from bs4 import BeautifulSoup
url = "https://www.amazon.in/AmazonBasics-Home-Safe-1-80-Cubic/dp/B078K2YPRW/?_encoding=UTF8&pd_rd_w=EiNHr&" \
      "content-id=amzn1.sym.b3717902-e6f3-48ab-a023-5a33abf60957&pf_rd_p=b3717902-e6f3-48ab-a023-5a33abf60957" \
      "&pf_rd_r=0STAWYDVG2928SPQ8EA6&pd_rd_wg=cwXuS&pd_rd_r=d0f563b2-f114-492a-b761-01f3f2294691&ref_=pd_gw_unk"

headers = {'Accept-Language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
sender_mail = "meinninjahattoriagyahun@gmail.com"
password = "r3dunicorn"
receiver_mail = "marioyakuza2000@gmail.com"


soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
price_int = price.split(",")
total_price = int(price_int[0])*1000 + int(price_int[1])
title = soup.find(id="productTitle").getText().strip()

BUY_PRICE = 90000
print(total_price)

if total_price < BUY_PRICE:
    message = f"{title} is now ₹{price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(sender_mail, password)
        connection.sendmail(
            from_addr=sender_mail,
            to_addrs=receiver_mail,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

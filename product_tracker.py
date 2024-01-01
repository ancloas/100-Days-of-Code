import requests 
from bs4 import BeautifulSoup
import re
from send_mail import send_mail

def extract_product_price(url, target_price: float):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    } 
    response= requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # get list of titles
    
    # price_element= soup.find_all(attrs={"class": "a-price-whole"})
    price_string= soup.select_one('#corePriceDisplay_desktop_feature_div .a-price-whole').string
    price= int(price_string.replace(',', ''))
    product_tile=soup.select_one('#productTitle').string

    
    if price< target_price:
        msg=f"""
Hi Anugrah,
    Alert for  product: {product_tile}
    hot_price: {price}
    target_price: {target_price}
    Link: {url} 
"""
        send_mail(subject=f'Alert for {product_tile}', msg_content=msg)
        return 'alerted user about the price'
    return 'price not low enought to notify the subject'
print(extract_product_price('https://amzn.eu/d/8rOSCnL', target_price=2000))
    
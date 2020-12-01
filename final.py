import bs4 as bs
import urllib.request
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import json

class ajio_care:
    def find_stock(url,size_lvl):
        ''' an automated stock finder'''
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        all_scripts = soup.find_all("script") #all associated scripts
        req_script = all_scripts[11]
        req_str= str(req_script)
        format1 = req_str.split("= ")
        str_final = format1[1].split(";")
        product_details = json.loads(str_final[0])
        return [product_details['product']['productDetails']['variantOptions'][size_lvl]['stock']['stockLevel'],product_details['product']['productDetails']['variantOptions'][2]['priceData']['formattedValue']]


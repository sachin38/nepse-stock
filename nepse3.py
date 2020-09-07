#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.nepalstock.com/company/" # Url to send post requests
    symbol = input("Enter Stock Symbol: ") # Taking symbol from user
    param = {"stock_symbol": symbol}

    req = requests.post(url,data=param,verify=False) # Sending Post request
    response = req.text
    soup = BeautifulSoup(response,"lxml")
    
    table = soup.find("table")
    print("\n")
    print("Company:"+table.findAll("td")[0].string)
    for row in table.findAll("tr")[4:]:
        col = row.findAll("td")
        print(col[0].string+" :"+col[1].string)

main()

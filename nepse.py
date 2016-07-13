#!/usr/bin/env python 
from bs4 import BeautifulSoup
import requests

print "Enter the stock Symbol: ",
symbol = raw_input()
url = "http://www.nepalstock.com/company/"
req = requests.post(url, data={"stock_symbol":symbol}, verify=False)
response = req.text
soup = BeautifulSoup(response, "lxml")
table = soup.find("table")
print "\n"
print "\n"
print "Company: ",table.findAll("td")[0].string
for row in table.findAll("tr")[4:]:
    col = row.findAll("td")
    print col[0].string,": ",col[1].string
print "\n"
print "\n"

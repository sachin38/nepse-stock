#!/usr/bin/env python 

"""
Copyright (C) 2017  Puskar Adhikari

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from bs4 import BeautifulSoup
import requests
import csv
# asking for stock symbol
symbol = raw_input("Enter the stock Symbol: ")
url = "http://www.nepalstock.com/company/"

try:
    #make post requests with that symbol and capture it in req 
    req = requests.post(url, data={"stock_symbol":symbol}, verify=False)
except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)

response = req.text
soup = BeautifulSoup(response, "lxml")
table = soup.find("table")
datas = []
print "\n"
print "\n"
print "Company: ",table.findAll("td")[0].string
for row in table.findAll("tr")[7:]:
    col = row.findAll("td")
    print col[0].string,": ",col[1].string
    datas.append(col[1].string)
    with open("datafile.csv", "a") as output:
        writer = csv.writer(output, quoting=csv.QUOTE_ALL)
        writer.writerow(datas)
        datas[:] = []
print "\n"
print "\n"

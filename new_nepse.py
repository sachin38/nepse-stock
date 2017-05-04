from bs4 import BeautifulSoup
import requests
import csv
import os.path

def fetchdata():
    symbol = raw_input("Enter the stock symbol: ")
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
    company_name = table.findAll("td")[0].string
    datas.append(company_name)
    for row in table.findAll("tr")[7:]:
        col = row.findAll("td")
        print col[0].string,": ",col[1].string
        datas.append(col[1].string)
   
    write_to_csv(datas)
    datas[:] = []

def write_to_csv(received_data = [], *args):
    first_data = ["Company", "Last Traded Price", "Change", "Total Listed Shares", "Paid Up Value", "Total Paid Up Value", "Closing Market Price", "Market Capitalization"]
    
    if os.path.isfile("datafile.csv"):
        with open("datafile.csv", "a") as output:
            writer = csv.writer(output, quoting=csv.QUOTE_ALL)
            writer.writerow(received_data)
            received_data[:] = []
    else:
        with open("datafile.csv", "w") as output:
            writer = csv.writer(output, quoting=csv.QUOTE_ALL)
            writer.writerow(first_data)
            writer.writerow(received_data)
            received_data[:] = []


fetchdata()

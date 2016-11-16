import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.nepalstock.com/company/" # Url to send post requests
    symbol = input("Enter Stock Symbol: ") # Taking symbol from user
    param = {"stock_symbol": symbol}

    req = requests.post(url,data=param,verify=False) # Sending Post request
    response = req.text
    soup = BeautifulSoup(response,"lxml")
    table_data = soup.find("table")
    print("\n=========================================\n")
    print("Company: "+table_data.findAll("td")[0].string)
    print("\n=========================================\n")

    for row in table_data.findAll("tr"):
        col = row.findAll("td")
        element = 0
        for data in col :
            print(data.string,end="")
            element += 1

            if element == 2:
                break

            print(" : ",end="")

        print("\n")

main()

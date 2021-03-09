"""
created by pangea2015 on GitHub

READ README.md BEFOR USING THE PROGRAM
ENTER YOUR API KEY FROM https://free.currencyconverterapi.com/ INTO api_key.ini FILE
MAKE SURE TO INSTALL ALL PACKAGES LISTED UNTER #Import BELOW
"""

# Import
from bs4 import BeautifulSoup
import requests
import datetime
import os
import json
import pandas as pd

# vars
score = 0
last_year = datetime.date.today() - datetime.timedelta(days=365) # calculates date last year

# Data
try:
    inflation_data = requests.get("http://www.leitzinsen.info/inflation.htm")
    interest_data = requests.get("http://www.leitzinsen.info/eurozone.htm") 
except:
    raise RuntimeError("Unable to access http://www.leitzinsen.info/")

with open("api_key.ini") as key:
    for line in key:
        try:
            usdeur_today = requests.get("https://free.currconv.com/api/v7/convert?q=USD_EUR&compact=ultra&apiKey=" + str(line))
            usdeur_y = requests.get("http://free.currconv.com/api/v7/convert?apiKey=" + str(line) + "&q=USD_EUR&compact=ultra&date=" + str(last_year))
        except:
            raise RuntimeError("Unable to access API")

# Functions
def is_month_right(): # Checks if the current month is between November and April.
    global score
    monthnow = int(datetime.datetime.now().strftime("%m"))
    if monthnow <= 4 and monthnow > 0:
        score += 1
    elif monthnow >= 11 and monthnow <= 12:
        score += 1
    else:
        raise ValueError('cannot calculate current month')
    return score

def dollar_euro(): # Checks if the Dollar has gone up in price in relation to the Euro in the last year.
    global score
    usdeur_today_value = json.dumps(usdeur_today.json()["USD_EUR"], indent=1)
    usdeur_y_value = json.dumps(usdeur_y.json()["USD_EUR"], indent=1)
    if usdeur_today_value > usdeur_y_value:
        score += 1
    elif usdeur_today_value < usdeur_y_value:
        score += 0
    else:
        raise ValueError
    return score

def get_interest(): # Checks if the latest change in interest rates by the EZB was a reduction.
    global score
    global interest_data
    sitetext = BeautifulSoup(interest_data.text, "html.parser")
    
    for pic in sitetext.findAll("img"):
        gif = pic.get("src")
        if ".gif" in gif:
            if "gleich" in gif:
                continue
            elif "unten" in gif:
                score += 1
            elif "oben" in gif:
                score += 0
            else:
                raise RuntimeError
            break
    return score

def get_inflation(): # checks if the inflation rate is lower than last year
    data = []
    global score
    global inflation_data
    sitetext = BeautifulSoup(inflation_data.text, "html.parser")
    table = sitetext.find("table", {"id" : ""})

    for row in table.find_all("tr"):
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    
    if data[1][1] < data[13][1]:
        score += 1
    elif data[1][1] >= data[13][1]:
        score += 0
    else:
        raise ValueError('Unable to calculate Inflation')
    return score

# Code
is_month_right()
dollar_euro()
get_interest()
get_inflation()

print("Score:", score) # shows the calculated score
if score <= 1 and score >= 0:
    print("Signal: Verkaufen!")
elif score == 2:
    print("Signal: keine Änderung")
elif score >= 3 and score <= 4:
    print("Signal: Kaufen!")
else:
    raise ValueError('"Score" out of range')

print("\n\n\n")
os.system("pause")

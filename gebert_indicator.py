"""
created by pangea2015 on GitHub

READ README.md BEFOR USING THE PROGRAM
ENTER YOUR API KEY FROM https://free.currencyconverterapi.com/ INTO api_key.ini FILE
"""

# Import
from bs4 import BeautifulSoup
from requests import get
from datetime import datetime, date, timedelta
import json
from argparse import ArgumentParser

# vars
score = 0
last_year = date.today() - timedelta(days=365) # calculates date last year

# Data
try:
    inflation_data = get("http://www.leitzinsen.info/inflation.htm")
    interest_data = get("http://www.leitzinsen.info/eurozone.htm") 
except:
    raise RuntimeError("Unable to access http://www.leitzinsen.info/")

with open("api_key.ini", "r") as f:
    for line in f:
        usdeur_today = get(f"https://free.currconv.com/api/v7/convert?q=USD_EUR&compact=ultra&apiKey={str(line)}")
        usdeur_y = get(f"http://free.currconv.com/api/v7/convert?apiKey={str(line)}&q=USD_EUR&compact=ultra&date={str(last_year)}")
        break

# Functions
def is_month_right(): # Checks if the current month is between November and April.
    global score
    monthnow = int(datetime.now().strftime("%m"))
    if monthnow <= 4 and monthnow > 0:
        score += 1
    elif monthnow >= 11 and monthnow <= 12:
        score += 1
    return monthnow

def dollar_euro(): # Checks if the Dollar has gone up in price in relation to the Euro in the last year.
    global score
    global usdeur_today_value
    global usdeur_y_value
    try:
        usdeur_today_value = json.dumps(usdeur_today.json()["USD_EUR"], indent=1)
        usdeur_y_value = json.dumps(usdeur_y.json()["USD_EUR"][str(last_year)], indent=1)
    except:
        raise RuntimeError("\n\n\n\n\nUnable to connect to https://free.currencyconverterapi.com/. Please try again later!")
    
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
    global score
    global inflation_data
    global data
    data = []
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

def calculate_signal():
    global score
    if score <= 1 and score >= 0:
        return "sell"
    elif score == 2:
        return "same"
    elif score >= 3 and score <= 4:
        return "buy"
    else:
        raise ValueError('"Score" out of range')

# score calculation
is_month_right()
dollar_euro()
get_interest()
get_inflation()

# arpgarse
parser = ArgumentParser(description="access all built-in calculations seperatly")
parser.add_argument("-s", "--score", help="current score", action="store_true")
parser.add_argument("-sig", "--signal", help="the corresponding signal (like buy, sell)", action="store_true")
parser.add_argument("-m", "--month", help="current month", action="store_true")
#parser.add_argument("-intr", "--interest", help="Eurozone interest rate", action="store_true") | WILL ADD LATER
parser.add_argument("-dexday", "--dextoday", help="Dollar / Euro exchange rate TODAY", action="store_true")
parser.add_argument("-dexyear", "--dexyear", help="Dollar / Euro exchange rate LAST YEAR", action="store_true")
parser.add_argument("-infday", "--infday", help="Inflation rate TODAY", action="store_true")
parser.add_argument("-infyear", "--infyear", help="Inflation rate LAST YEAR", action="store_true")
args = parser.parse_args()

if args.score:
    print(score)
if args.signal:
    print(calculate_signal())
if args.month:
    print(is_month_right())
if args.dextoday:
    dollar_euro()
    print(usdeur_today_value)
if args.dexyear:
    dollar_euro()
    print(usdeur_y_value)
if args.infday:
    get_inflation()
    print(data[1][1])
if args.infyear:
    get_inflation()
    print(data[13][1])


# score output
if __name__ == "__main__":
    if not any(vars(args).values()):
        print(f"Score: {score}") # shows the calculated score
        print(f"Signal: {calculate_signal()}\n") # shows corresponding signal

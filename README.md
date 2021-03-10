# Gebert Indicator
### What is the Gebert Indicator?
The Gebert stock market Indicator was invented by the german physicist Thomas Gebert in the 1990s, and can help you invest in german stock indecies, just as the DAX. Using the Gebert Indicator would have granted you a significantly higher return on Investment. 

### How did it perform?

![Chart](https://upload.wikimedia.org/wikipedia/commons/4/4f/Entwicklung_des_DAX_und_Verm%C3%B6genszuwachs_nach_dem_Gebert-System_von_1992_bis_2019.jpg)
>Long term chart comparing the Gebert Indicator and the DAX. (in percent %)

![Periods](https://upload.wikimedia.org/wikipedia/commons/6/61/DAX-Chart_von_1988_bis_2018_mit_Gebert-Investitionsphasen.jpg)
>Chart of the periods in which you would have been invested in the market (green).

As you propably can see, just by using this Strategy, you would have gained over 3000% return on your investment. The DAX, the index we invested in, made "only" 750% in the same period of time.

### How does it work?
As amazing the return is, as simple it is to do. The Gebert Indicator works with a 4-Point score system of so called "sub-indicators".
You can simply buy an DAX ETF at low costs, to maximise your profit.
> Due to this being on a monthly basis, you need to recalculate EVERY month!

* Eurozone Interest rates
    * If the latest interest rate hike by the ECB was a cut, this means you add one point to the score, if it was an upward one, there are zero points.
* Eurozone Inflation
    * If the inflation rate determined by Eurostat for the Eurozone is below that of the same month of the previous year, this also means a point added to our score. A tie in inflation or an increase in a twelve-month comparison, on the other hand, are rated with zero points.
* Dollar-Euro exchange rate
    * If the US dollar is quoted in euros above its level twelve months ago, this results in one point, while an exchange rate that is the same or lower is rated as zero.
* Season
    * True to the motto “Sell in May and go away, stay away till St. Leger Day”, a point is added for the period from November 1st to April 30th, but not in any other months.

Now, lets see what to do at which score:

Score | Signal
----- | ------
0 | strong Sell 
1 | Sell
2 | no change
3 | Buy
4 | strong Buy


### Risks
As everyone knows, there is no free lunch in the world of Wallstreet. So how risky is this investment?

* The most important: It only works for the GERMAN stock market.
* The Gebert Indicator requires great discipline, because of the famous "Fear of Missing out", that can arise.
* The signals CAN'T be used for short positions, because they aren't precise enough.
* A rather uniqe role in this equasion plays the ECB, because it can severely impact your investment. Rises in interest rates by the ECB could have negative effects on your portfolio.

#### Further Informations: 
>https://de.wikipedia.org/w/index.php?title=Gebert-Indikator&oldid=208773021
> (There is only a german Wikipedia article on this topic, so just use Google Translate.)

> Sometimes, https://free.currencyconverterapi.com/ has server downtimes which will result an error message.

>THIS IS NO FINANCIAL ADVISE! 

# How does this Program work, and how do I use it?
## Tutorial
0. Before opening any file, visit https://free.currencyconverterapi.com/ , and get yourself an API Key!
1. Next up, you paste your key into the `api_key.ini` file.
2. To successfully start the `gebert_indicator.py` file, check if you have installed: `Beautifulsoup4`, `requests` and `pandas`
3. Now, just simply run `gebert_indicator.py`, and it will output you the current score, you then can use!

## Using "argprarse"
[![help.png](https://i.postimg.cc/c4PRPkXJ/help.png)](https://postimg.cc/qzX63wff)

> On the picture above, you can see the screen, that will appear, if you dont open the file directly.
> Instead use `-h` or `--help` after the file name in your CMD.

> just open CMD in your installation directory, and type: `gebert_indicator.py -h`

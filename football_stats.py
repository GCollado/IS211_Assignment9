"""
Part I ­ CBS Football Stats

1. Go to the CBS NFL Stats webpage, located at http://www.cbssports.com/nfl/stats
2. Under “PLAYER STATISTICS”,click on the Touchdowns links
3. Change the drop down to regular
4. Write a script called “football_stats.py” that will:
    a) load this URL
    b) parse it using BeautiulSoup,
    c) and output the list of top 20 players,including the player’s position, team and total number of touchdowns
"""

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns"

soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")

trs = soup.find_all('tr')
top20 = []
for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get('href')

    tds = tr.find_all("td")
    try:
        player = str(tds[0].get_text())
        pos = str(tds[1].get_text())
        team = str(tds[2].get_text())
        TD_total = str(tds[6].get_text())
    except:
        #print("Bad tr string: {}".format(tds))
        continue
    top20.append([player, pos, team, TD_total])
print("Top 20 Players By TouchDowns")
print("|{} |{}       |{}  |{}  |".format("ranking","Player", "Position", "TD"))
for ranking, player in enumerate(top20, 1):
    if ranking <= 20:
        print("|{}     |  {}|     {}| {}|".format(ranking, player[0], player[1], player[2], player[3]))
        

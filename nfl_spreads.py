"""
Part II - NFL Spread
1. Go to the current spreads link:
     http://www.footballlocks.com/nfl_point_spreads.shtml
2. Write a script called "nfl_spreads.py" that:
    a) loads this URL
    b) parse it using BeautifulSoup
    c) and output the given game's favorite, underdog and the spread
"""

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib.request

url = "http://www.footballlocks.com/nfl_point_spreads.shtml"

soup = BeautifulSoup(urllib.request.urlopen(url), features='lxml')

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('td'):
        print(link)

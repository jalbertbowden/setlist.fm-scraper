from urllib import urlopen
 
optionsUrl = 'http://www.setlist.fm/venue/the-boathouse-norfolk-va-usa-2bd6387a.html'
optionsPage = urlopen(optionsUrl)
from bs4 import BeautifulSoup
soup = BeautifulSoup(optionsPage)
b = soup.find_all("div", class_="row contentBox visiblePrint")
print b
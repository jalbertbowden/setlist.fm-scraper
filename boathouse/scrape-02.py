from urllib import urlopen
from bs4 import BeautifulSoup
import json


optionsUrl = 'http://www.setlist.fm/venue/the-boathouse-norfolk-va-usa-2bd6387a.html'
optionsPage = urlopen(optionsUrl)
soup = BeautifulSoup(optionsPage, 'lxml')

concerts = []

entries = soup.find_all("div", class_="col-xs-12 setlistPreview vevent") # a list
for entry in entries:
	concert = {}
	concert['date'] = entry.find('span', class_="value-title")['title']
	
	# strip out at The Boathouse, Norfolk, VA in bands
	# find out what prepended u' is in bands and get rid of it
	concert['artist'] = entry.find('a', class_="summary url").find("span").text.strip()
	tour = entry.find('a', attrs={"rel":"nofollow"})
	# this is a hack -> its fragile, will break -> find a new selector   talking about code below!!!
	if len(tour) == 1:
		concert['tour'] = entry.find('a', attrs={"rel":"nofollow"}).text.strip() # this selector needs to be more specific
	else:
		concert['tour'] = ''
	concert['setlist'] = [link.text for link in soup.select("div > ol > li")]

# find breadcrumbs, get last one
# ul.listPagingNavigator text-center hidden-print
# last one is ul li a -> title="Go to last page"
# href="../venue/the-boathouse-norfolk-va-usa-2bd6387a.html?page=52




	concerts.append(concert)




print concerts


#print b

# span.month, span.day, span.year, span.value-title HAS title-attribute with date....
#dates = b.find_all("span", class_="value-title")
#for 
#print dates
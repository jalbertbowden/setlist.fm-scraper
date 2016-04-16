from lxml import html
import requests
import json

# Next we will use requests.get to retrieve the web page with our data, parse it using the html module and save the results in tree:
# http://www.setlist.fm/venue/the-boathouse-norfolk-va-usa-2bd6387a.html
# http://econpy.pythonanywhere.com/ex/001.html
page = requests.get('http://www.setlist.fm/venue/the-boathouse-norfolk-va-usa-2bd6387a.html')
tree = html.fromstring(page.content)


#This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')

# condensed dateBlock dtstart
showDateMonth = tree.xpath('//span[@class="month"]/text()')
showDateDay = tree.xpath('//span[@class="day"]/text()')
showDateYear = tree.xpath('//span[@class="year"]/text()')
showDate = tree.xpath('//span[@class="value-title"]/@title') #you want this title value

# get show headline


#Let's see what we got exactly:
# print 'Show Date Month: ', showDateMonth
# print 'Show Date Day: ', showDateDay
# print 'Show Date Year: ', showDateYear
# print 'Show Date: ', showDate
# print 'Buyers: ', buyers
# print 'Prices: ', prices
jsonOutputA = 'Show Date Month: ', showDateMonth
jsonOutputB = 'Show Date Day: ', showDateDay
jsonOutputC = 'Show Date Year: ', showDateYear
jsonOutputD = 'Show Date: ', showDate

jsonOutput = '{', jsonOutputA ,'},{', jsonOutputB ,'},{', jsonOutputC ,'},{', jsonOutputD ,'}'

with open('setlist-01.json', 'w') as outfile:
	json.dump(jsonOutput, outfile)

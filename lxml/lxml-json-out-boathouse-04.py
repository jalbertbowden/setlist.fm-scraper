from lxml import html
import requests
import json

# Next we will use requests.get to retrieve the web page with our data, parse it using the html module and save the results in tree:
# http://www.setlist.fm/venue/the-boathouse-norfolk-va-usa-2bd6387a.html
page = requests.get('http://www.setlist.fm/venue/the-boathouse-norfolk-va-usa-2bd6387a.html')
tree = html.fromstring(page.content)

# get show dates from span classes
showDateMonth = tree.xpath('//span[@class="month"]/text()')
showDateDay = tree.xpath('//span[@class="day"]/text()')
showDateYear = tree.xpath('//span[@class="year"]/text()')
showDate = tree.xpath('//span[@class="value-title"]/@title') #you want this title value

# get show headline
showHeadline = tree.xpath('//div[@class="row contentBox visiblePrint"]/div/div/h2/a/text()')
# setListFMURL = "http://www.setlist.fm/"
# need to prepend this url in infront of showHeadlineSetListURL, as well as strip out leading "../" in the href attribute values...
showHeadlineSetListURL = tree.xpath('//div[@class="row contentBox visiblePrint"]/div/div/h2/a/@href')


# div.details span[Artist: ]
# div.details span[Tour: ]
# div.details span[Venue: ]
# div.setSummary

#get artist value
showArtist = tree.xpath('//span[contains(text(),"Artist:")]/strong/a//span/text()')
showTour = tree.xpath('//span[contains(text(),"Tour:")]/strong/a/text()')
#get venue value
#get setlist values
#get breadcrumbs values

# print 'Show Date Month: ', showDateMonth
# print 'Show Date Day: ', showDateDay
# print 'Show Date Year: ', showDateYear
# print 'Show Date: ', showDate
# print 'Show Headline: ', showHeadline
# print 'Show Headline Setlist Link: ', showHeadlineSetListURL
# print 'Show Artist: ', showArtist
# print 'Show Tour: ', showTour


jsonOutputA = 'Show Date Month: ', showDateMonth
jsonOutputB = 'Show Date Day: ', showDateDay
jsonOutputC = 'Show Date Year: ', showDateYear
jsonOutputD = 'Show Date: ', showDate
jsonOutputE = 'Show Headline: ', showHeadline
jsonOutputF = 'Show Headline Setlist Link: ', showHeadlineSetListURL
jsonOutputG = 'Show Artist: ', showArtist
jsonOutputH = 'Show Tour: ', showTour

jsonOutput = '{', jsonOutputA ,'},{', jsonOutputB ,'},{', jsonOutputC ,'},{', jsonOutputD ,'},{', jsonOutputE ,'},{', jsonOutputF ,'},{', jsonOutputG ,'},{', jsonOutputH ,'}'

with open('setlist-04.json', 'w') as outfile:
	json.dump(jsonOutput, outfile)

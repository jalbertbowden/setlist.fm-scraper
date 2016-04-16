from lxml import html
import requests
import json

setlistFMURLCOM = "http://setlist.fm/"
venueShowsResultsURLDomain = setlistFMURLCOM + "venue/the-boathouse-norfolk-va-usa-2bd6387a.html";
venueShowsResultsURLKey = "?page="
veneuShowsResultsURL = venueShowsResultsURLDomain + venueShowsResultsURLKey


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

#get artist value
showArtist = tree.xpath('//span[contains(text(),"Artist:")]/strong/a//span/text()')
showTour = tree.xpath('//span[contains(text(),"Tour:")]/strong/a/text()')
showVenue = tree.xpath('//span[contains(text(),"Venue:")]/strong/a/span/text()')
showSetList = tree.xpath('//div[@class="setSummary"]/ol[@class="list-inline"]/li/text()')
# get setList doesn't seem to be associated to the band that played it....
# could be bc only one one this page i'm scraping...need to test a better example

showTotalDocuments = tree.xpath('//ul[@class="listPagingNavigator text-center hidden-print"]/li/a[@title="Go to last page"]/text()')

# now need to crawl all the documents = showTotalDocuments - 1
# define url, append document variable as you go up in for loop




# print 'Show Date Month: ', showDateMonth
# print 'Show Date Day: ', showDateDay
# print 'Show Date Year: ', showDateYear
# print 'Show Date: ', showDate
# print 'Show Headline: ', showHeadline
# print 'Show Headline Setlist Link: ', showHeadlineSetListURL
# print 'Show Artist: ', showArtist
# print 'Show Tour: ', showTour
# print "Show Venue: ", showVenue
# print "Show Setlist: ", showSetList
# print "Go to Last Page Value: ", showTotalDocuments
# working...but still injecting [''] around xxx variable...need to put an end to that shitte
# print "String Variable Concatentation #02: ", veneuShowsResultsURL + str(showTotalDocuments)

jsonOutputA = 'Show Date Month: ', showDateMonth
jsonOutputB = 'Show Date Day: ', showDateDay
jsonOutputC = 'Show Date Year: ', showDateYear
jsonOutputD = 'Show Date: ', showDate
jsonOutputE = 'Show Headline: ', showHeadline
jsonOutputF = 'Show Headline Setlist Link: ', showHeadlineSetListURL
jsonOutputG = 'Show Artist: ', showArtist
jsonOutputH = 'Show Tour: ', showTour
jsonOutputI = 'Show Venue: ', showVenue
jsonOutputJ = 'Show Setlist: ', showSetList
jsonOutputK = 'Go to Last Page Value: ', showTotalDocuments # definitely don't need this in json
jsonOutputL = 'String Variable Concatenation #02: ', veneuShowsResultsURL + str(showTotalDocuments)


jsonOutput = '{', jsonOutputA ,'},{', jsonOutputB ,'},{', jsonOutputC ,'},{', jsonOutputD ,'},{', jsonOutputE ,'},{', jsonOutputF ,'},{', jsonOutputG ,'},{', jsonOutputH ,'},{', jsonOutputI ,'},{', jsonOutputJ ,'},{', jsonOutputK ,'},{', jsonOutputL ,'}'

with open('setlist-07.json', 'w') as outfile:
	json.dump(jsonOutput, outfile)

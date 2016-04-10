from lxml import html
import requests

setlistFMURLCOM = "http://setlist.fm/"
venueShowsResultsURLDomain = setlistFMURLCOM + "venue/the-boathouse-norfolk-va-usa-2bd6387a.html";
venueShowsResultsURLKey = "?page="
venueShowsResultsURL = venueShowsResultsURLDomain + venueShowsResultsURLKey


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

showLastBreadcrumbURL = tree.xpath('//ul[@class="listPagingNavigator text-center hidden-print"]/li/a[@title="Go to last page"]/@href')
# now need to crawl all the documents = showTotalDocuments - 1
# define url, append document variable as you go up in for loop

# need to strip last page's numeric value
# then subtract by 1 (current page's value)
# run for loop, injecting var document number per loop

# then print/save as json/csv

venueShowsResultsDocuments = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
venueShowsResultsDocumentsTotal = showTotalDocuments
for documentPageNumber in range(len(venueShowsResultsDocuments)):
	print venueShowsResultsURL + str(documentPageNumber)

# this needs fixing

from urllib import urlopen
 
optionsUrl = 'http://finance.yahoo.com/q/op?s=AAPL+Options'
optionsPage = urlopen(optionsUrl)
from bs4 import BeautifulSoup
soup = BeautifulSoup(optionsPage)
print soup
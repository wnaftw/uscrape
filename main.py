#UrlScraper

import urllib2
from scrape import *
from iterate import *

#How to download images
f = open("test.gif", "wb")
f.write(urllib2.urlopen("http://webhost.salford.ac.uk/images/university-of-salford-logo.gif").read())
f.close()

urlList = []
site = urllib2.urlopen("http://www.cse.salford.ac.uk/physics/resources.php")
html = site.read()

scrape(html, urlList)

print len(urlList)

#for i in range(0, len(urlList)):
#    print urlList[i]

iterate(urlList, 150)

for i in range(0, len(urlList)):
    print urlList[i]
    
print len(urlList)

scrapeHTML(urlList)
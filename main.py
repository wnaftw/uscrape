#UrlScraper

import urllib2
from scrape import *
from iterate import *

url = ""
#How to download images
f = open("test.gif", "wb")
f.write(urllib2.urlopen(url).read())
f.close()

urlList = []
site = urllib2.urlopen(url)
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
#Iterate over list and scrape more urls

from scrape import *
import urllib2

def iterate(urlList, n):
    if len(urlList) >= 1:
        for i in range(0, len(urlList)):
            #CATCH UNSUPPORTED LINKS
            print "ATTEMPT: %s" % (urlList[i])
            if urlList[i][-1] == 'd':
                print "Not supported"
                continue
            elif urlList[i].find('"') != -1 or urlList[i].find(".js") != -1:
                print "Not supported"
                continue
            html = urllib2.urlopen(urlList[i]).read()
            scrape(html, urlList)
            if len(urlList) > n:
                break

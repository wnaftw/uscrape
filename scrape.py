# Read and store urls

import urllib2, os

def scrape(rawHtml, urlList):
    
    while rawHtml.find("http://") != -1:
        
        start = rawHtml.find("http://")
        rawHtml = rawHtml[start:]
    
        end = rawHtml.find('">')
        url = rawHtml[:end]
        urlList.append(url)
        rawHtml = rawHtml[end:]
        

def scrapeHTML(urlList):
    for i in range(0, len(urlList)):
        name = "html/" + str(i) + ".html"
        print "Attempt: %s" % (urlList[i])
        if urlList[i][-1] == 'd':
                print "Not supported"
                continue
        elif urlList[i].find('"') != -1 or urlList[i].find(".js") != -1:
                print "Not supported"
                continue
        try:
            rawHtml = urllib2.urlopen(urlList[i]).read()
            f = open(name, "w")
            f.write(rawHtml)
            f.close()
            print os.path.exists("html")
        except urllib2.URLError:
            print "Oops! Could not access site!"
            
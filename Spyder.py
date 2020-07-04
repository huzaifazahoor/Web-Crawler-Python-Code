#!/usr/bin/env python

import requests #To get requests
import re #Regular Expression
import urlparse #For Parsing

targetUrl = "https://google.com"
targetLinks = []

def extractLinks(url)
    response = requests.get(url)
    hrefLinks = re.findall('(?:href=")(.*?)"', response.content) #Regular Expressions to get only href

def crawl(url):
    hrefLinks = extractLinks(url) #Function call
    for link in hrefLinks:
        link = urlparse.urljoin(url, link) #Join target url with links

        if "#" in link:
            link = link.split("#")[0]
        
        if targetUrl in link and link not in targetLinks: #Only get target websites links
            targetLinks.append(link)
            print(link)
            crawl(link) # For recursion to find more links
            
crawl(targetUrl)
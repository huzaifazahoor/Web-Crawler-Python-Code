#!/usr/bin/env python

import requests #To get requests

def request(url):
    try:
        return requests.get("http://" + url) #Get response from url
    except requests.exceptions.ConnectionError: #Exception for Wrong subdomain
        pass
        

targetUrl = "google.com"

with open("Subdomains.txt", "r") as wordlistFile: #path of wordlist
    for line in wordlistFile:
    word = line.strip() #For get the line in file
        testUrl = word + "." + targetUrl
        response = request(testUrl) #for response
        if response:
            print("[+] Discovered subdomains --> " + testUrl)
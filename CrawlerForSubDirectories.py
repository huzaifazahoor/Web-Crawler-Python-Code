#!/usr/bin/env python

import requests #To get requests

def request(url):
    try:
        return requests.get("http://" + url) #Get response from url
    except requests.exceptions.ConnectionError: #Exception for Wrong subdomain
        pass
        

targetUrl = "google.com" #target

with open("C:\Users\Hp\Downloads\Video\Udemy - Learn Python & Ethical Hacking From Scratch\17. Website Hacking - Writing a Crawler\SubDir.txt", "r") as wordlistFile: #path of wordlist
    for line in wordlistFile:
    word = line.strip() #For get the line in file
        testUrl = targetUrl + "/" + word
        response = request(testUrl) #for response
        if response:
            print("[+] Discovered subdomains --> " + testUrl)
#!/usr/bin/env python

import requests
import lxml.html
from bs4 import BeautifulSoup
import urllib2
import re
# import pyexcel

#Opening the main page, with contaings the school urls which will be scrapped
urlMain = 'http://redeemancipa.org.br/institucional/quem-somos/'
htmlMain = requests.get(urlMain).content
soupMain = BeautifulSoup(htmlMain, 'lxml')

listNames = []
listGeneralInfo = []

#Extract the URL of each school from the main HTML
for i in soupMain.select('.cursList'):
    schoolURL = i.find('a').attrs['href']
    URLnumber = re.findall(r'\d+',schoolURL)
    #Open each URLs and read it in BeautifulSoup
    for n in URLnumber:
        address = ('http://redeemancipa.org.br/?page_id=' + n)
        html = urllib2.urlopen(address).read()
        soup = BeautifulSoup(html, "lxml")

        tagContent = soup.select('.textContent')
        #Sraping the name of each school
        for schoolName in tagContent:
            listNames.append(schoolName.find('h2').text)
        # Scrapping the general information of each school

        generalInfo = soup.find('meta', attrs={'property': 'og:description'})
        listGeneralInfo.append(generalInfo['content'].strip())

        #next step: search for the address inside the list listaGeneralInfo
        
        test = zip(listNames, listGeneralInfo)

exportData = pyexcel.save_as(array = test, dest_file_name = "teste.csv")

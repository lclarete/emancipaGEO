import requests
import lxml.html
from bs4 import BeautifulSoup
import urllib2
import re

urlMain = 'http://redeemancipa.org.br/institucional/quem-somos/'

urlMain_request = requests.get(urlMain)
htmlMain = urlMain_request.content
soupMain = BeautifulSoup(htmlMain, 'lxml')

listURLs = []
listTitle = []
listMail1 = []
listMail2 = []
listLocation1 = []
listLocation2 = []

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
            listTitle.append(schoolName.find('h2').text)

print listTitle


# for url in listURLs:
#     url_request = urllib2.urlopen(url)
#     soup = BeautifulSoup(url_request, "lxml")
#     for item in soup.findAll('.textContent'):
#         listTitle.append(item.find('h2').text)
#
# print listTitle
#
# for x in listURLs:
#     tagContent = soup.findAll('div', {'class':'textContent'})
#     listTitle.append(t.find('h2'))

# for m1 in soup.findAll('div', {'class':'menu'}):
#     listMail2.append(m1.find('p'))
#
# for m2 in soup.findAll('div', {'dir':'ltr'}):
#     mail2 = m2.findAll('a')[2]
#     listMail1.append(mail2.attrs['href'])
#
# for l1 in soup.findAll('div', {'class':'blockContent'}):
#     location1 = l1.findAll('p')[1].text
#     listLocation1.append(location1)
#
# for l2 in soup.findAll('div', {'dir':'ltr'}):
#     location2 = l2.findAll('p')[4].text
#     listLocation2.append(location2)
#
# print listTitle, listMail2, listMail1, listLocation1, listLocation2

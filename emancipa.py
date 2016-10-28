import requests
import lxml.html
from bs4 import BeautifulSoup

urlMain = 'http://redeemancipa.org.br/institucional/quem-somos/'

url_request = requests.get(urlMain)
html = url_request.content
soupMain = BeautifulSoup(html, 'lxml')

listPages = listTitle = listMail1 = listMail2 = listLocation1 = listLocation2 = []

#Extract the URL of each school from the main HTML page
for i in soupMain.select('.cursList'):
    listPages.append(i.find('a').attrs['href'])

for t in soup.findAll('div', {'class':'textContent'}):
    listTitle.append(t.find('h2').text)

for m1 in soup.findAll('div', {'class':'menu'}):
    listMail2.append(m1.find('p'))

for m2 in soup.findAll('div', {'dir':'ltr'}):
    mail2 = m2.findAll('a')[2]
    listMail1.append(mail2.attrs['href'])

for l1 in soup.findAll('div', {'class':'blockContent'}):
    location1 = l1.findAll('p')[1].text
    listLocation1.append(location1)

for l2 in soup.findAll('div', {'dir':'ltr'}):
    location2 = l2.findAll('p')[4].text
    listLocation2.append(location2)

print listTitle, listMail2, listMail1, listLocation1, listLocation2



import requests
import json
import time
url = "https://www.ascap.com/repertory#ace/search/workID/894535922" 
url = "https://www.ascap.com/repertory#ace/search/workID/894535922"

#r = requests.post(url, data=json.dumps(data), headers=headers)
#r = requests.post(url)
#print (r.status_code)
#print (r.content)
#print (r.json())

# The page is rendered with JavaScript making more requests to fetch additional data. 

# body, div, div "mainContent", div role="main", div class="pdynamicbutton", a class=call role=button>Agree and Proceed<

from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('C:\\Program Files (x86)\\nodejs\\chromedriver.exe')

#<div class="workID">
# Work ID:
# <span>
#  80031416
# </span>
#</div>
# returns 80031416
def getWorkId(soup):
    workIdElement = soup.find("div", {"class": "workID"})
    spanElement = workIdElement.find("span")
    return spanElement.text.strip()

#<div class="card__header__title">
# HERE
# <span class="card__header__title--ascap">
#  Total Current ASCAP Share:
#        99.98%
# </span>
#</div>
# returns HERE
def getTrackTitle(soup):
    headerTitleElement = soup.find("div", {"class": "card__header__title"})
    innerHtml = str(headerTitleElement.encode_contents()) # similar to DOM innerHtml
    innerHtmlSplit = innerHtml.split('<')[0].strip()
    innerHtmlSplit = innerHtmlSplit.split('\\n')
    return innerHtmlSplit[1].strip()
    
#    <div class="creditors" id="performers">
#     <div class="creditors__title">
#      Performers
#      <span class="performer-count">
#       (1)
#      </span>
#     </div>
#     <div class="creditors__list">
#      <div class="creditor">
#       BENNETT T
#      </div>
def getFirstPerformer(soup):
    performersElement = soup.find("div", {"id": "performers"})
    performerElement = performersElement.find("div", {"class": "creditor"})
    return performerElement.text.strip()

def getSoupPageFromAscap(workId, sleepTimeSeconds):
    url = "https://www.ascap.com/repertory#ace/search/workID/" + str(workId)
    print('getSoupPageFromAscap', url)
    driver.get(url)
    time.sleep(sleepTimeSeconds)
    soup = BeautifulSoup(driver.page_source, 'html.parser')    
    return soup

def clickElement(element):
    print('clickElement', element)
    if element != None:
        element.click()
        time.sleep(5)
    else:
        print("Cannot click")
        
### This does not work!!
def clickOKAgreeBanners(soup):
    clickElement(soup.find('button', text='I AGREE'))
    clickElement(soup.find('a', text='AGREE AND PROCEED'))
    time.sleep(2)  
        
def getTrackData(soup):
    firstPerformer = getFirstPerformer(soup)
    print('firstPerformer', firstPerformer)
    
    workId = getWorkId(soup)
    print('workId', workId)
    
    trackTitle = getTrackTitle(soup)
    print('trackTitle', trackTitle)
        
soup = getSoupPageFromAscap(894535922, 6) # STREET AT NIGHT from PRHYME
#clickOKAgreeBanners(soup)                  # does not work

getTrackData(getSoupPageFromAscap(390222285, 1)) # I Love from LENNON SISTERS
getTrackData(getSoupPageFromAscap(80031416, 1))  # HERE from BENNETT T

driver.quit()

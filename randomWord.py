import requests
from bs4 import BeautifulSoup
import lxml
import random

def getWebR(urls):
    url = urls
    r = requests.get(url)
    r = r.text
    return(r)

def parseData(r):
    soup = BeautifulSoup(r, features='lxml')
    allText = soup.findAll('p')
    allText = [x.text for x in allText]
    allText = str(allText[0])
    allText = allText.splitlines()
    return(allText)

def createRandom(wordList):
    length = len(wordList)
    randomNR = random.randint(0, (length-1))
    return[wordList[randomNR]]
    

print(createRandom(parseData(getWebR('http://norvig.com/ngrams/sowpods.txt'))))








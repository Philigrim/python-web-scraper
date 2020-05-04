from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from wrBooks import writingToFile
from threading import Thread


def getCategoriesUrls(mainUrl, limit):
    page = urlopen(mainUrl)
    htmlFull = page.read()
    page.close()
    htmlClear = BeautifulSoup(htmlFull, 'html.parser')

    urlsListsDiv = htmlClear.find('div', {'class':'content-right'})
    aTags = urlsListsDiv.findAll('a')
    
    categoriesUrls = []
    i = 1
    for tag in aTags:
        categoriesUrls.append(mainUrl + tag.get('href'))
        if i==limit:
            return categoriesUrls
        i=i+1

def getBooksUrls(mainUrl, url, bookUrls, limit):
    page = urlopen(url)
    htmlFull = page.read()
    page.close()
    htmlClear = BeautifulSoup(htmlFull, 'html.parser')

    booksField = htmlClear.find('div', {'id':'row'})
    bookATags = booksField.findAll('a', {'class': 'boook'})

    i = 1
    for tag in bookATags:
        bookUrls.append(mainUrl + tag.get('href'))
        if i==limit:
            return bookUrls
        i=i+1

def getBookData(url):
    page = urlopen(url)
    htmlFull = page.read()
    page.close()
    htmlClear = BeautifulSoup(htmlFull, 'html.parser')

    bookField = htmlClear.find('div', {'class':'product-details'})

    author = bookField.find('h2').getText()
    title = bookField.find('span', {'itemprop':'name'}).getText()
    releaseDate = bookField.find('span', {'itemprop':'datePublished'}).getText()
    category = bookField.findAll('a')[3].getText()
    username = bookField.findAll('a')[1]['title']
    priceConditionCityDiv = bookField.find('div', {'class':'col-sm-6 offer-info'})
    
    i = 0
    city = "Nenurodyta"
    condition = "Nenurodyta"
    price = "Nenurodyta"
    for word in priceConditionCityDiv.getText().split():
        if word == "€":
            price = priceConditionCityDiv.getText().split()[i+1]
        elif word == "Miestas:":
            city = priceConditionCityDiv.getText().split()[i+1]
        elif word == "Būklė:":
            if priceConditionCityDiv.getText().split()[i+1] == "Labai":
                condition = priceConditionCityDiv.getText().split()[i+1] + ' ' + priceConditionCityDiv.getText().split()[i+2]
            else:
                condition = priceConditionCityDiv.getText().split()[i+1]
        i=i+1

    if bookField.find('label', {'itemprop':'comment'}) != None:
        comment =  bookField.find('label', {'itemprop':'comment'}).getText()[12:].replace('\n', '').replace('\r', ' ')
    else:
        comment = "-"

    bookData = []
    bookData.append(title)
    bookData.append(author)
    bookData.append(releaseDate)
    bookData.append(category)
    bookData.append(username)
    bookData.append(city)
    bookData.append(price)
    bookData.append(condition)
    bookData.append(comment)
    
    return bookData

def dataToJson(bookData):
    jsonData = {}
    jsonData["title"] = bookData[0]
    jsonData["author"] = bookData[1]
    jsonData["releaseDate"] = bookData[2]
    jsonData["category"] = bookData[3]
    jsonData["username"] = bookData[4]
    jsonData["city"] = bookData[5]
    jsonData["price"] = bookData[6]
    jsonData["condition"] = bookData[7]
    jsonData["comment"] = bookData[8]

    return jsonData


def getBooksDataFromCategor(mainUrl, categoriesUrls, booksWantedFromOneCategory, booksData, isMultiThread):
    if isMultiThread:
        booksUrls = []
        getBooksUrls(mainUrl, categoriesUrls, booksUrls, booksWantedFromOneCategory)

        for bookUrl in booksUrls:
            booksData.append(getBookData(bookUrl))
    else:
        booksUrls = []
        for categoriesUrl in categoriesUrls:
            getBooksUrls(mainUrl, categoriesUrl, booksUrls, booksWantedFromOneCategory)

        for bookUrl in booksUrls:
            booksData.append(getBookData(bookUrl))


def runScrape(url, newBooksFile, categoriesWanted, booksWantedFromOneCategory, isMultiThread):
    if isMultiThread:
        categoriesUrls = getCategoriesUrls(url, categoriesWanted)

        booksData = []
        threads = []

        for categoriesUrl in categoriesUrls:
            t = Thread(target=getBooksDataFromCategor, args=(url, categoriesUrl, booksWantedFromOneCategory, booksData, isMultiThread,))  
            t.start()
            threads.append(t)

        for oneThread in threads:
            oneThread.join()

        jsonDataList = []
        for bookData in booksData:
            jsonDataList.append(dataToJson(bookData))

        writingToFile.createFile(newBooksFile, jsonDataList)
        
    else:
        categoriesUrls = getCategoriesUrls(url, categoriesWanted)

        booksData = []
        getBooksDataFromCategor(url, categoriesUrls, booksWantedFromOneCategory, booksData, isMultiThread)

        jsonDataList = []
        for bookData in booksData:
            jsonDataList.append(dataToJson(bookData))

        writingToFile.createFile(newBooksFile, jsonDataList)
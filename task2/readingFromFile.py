import book
import seller
import bookAd

import json
import os

class Reading:
    books = []
    sellers = []
    bookAds = []
    
    def __init__(self, fileName):
        books = []
        sellers = []
        bookAds = []
        with open(fileName, "r") as bookAdsFile:
            for oneBookAd in bookAdsFile:
                bookAdLine = json.loads(oneBookAd)
                newBook = book.Book.createBookObject(bookAdLine["title"],bookAdLine["author"],bookAdLine["releaseDate"],bookAdLine["category"])
                newSeller = seller.Seller(bookAdLine["username"], bookAdLine["city"])
                newBookAd = bookAd.BookAd(newBook, newSeller, bookAdLine["price"], bookAdLine["condition"], bookAdLine["comment"])
                books.append(newBook) 
                sellers.append(newSeller) 
                bookAds.append(newBookAd)
        self.books = books
        self.sellers = sellers
        self.bookAds = bookAds
    
    def getBooks(self):
        return self.books
    def getSellers(self):
        return self.sellers
    def getBookAds(self):
        return self.bookAds

    def printInformationAboutFile(self):
        print("File contains " + str(len((self.bookAds))) + " book ads.")
        print(str(book.Book.getDifferentBooksCount(self.books)) + " different books were uploaded by " + str(len(seller.Seller.getDifferentRecords(self.sellers, "username"))) + " users.")
        print("Uploaders are from " + str(len(seller.Seller.getDifferentRecords(self.sellers, "city"))) + " different cities.")
            
    
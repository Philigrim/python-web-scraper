import json
import os

from bookClasses import leisureBook, familyHealthKidsBook, documentaryBook, scientificBook, textbook, foreignBook, otherBook
from bookClasses import seller
from bookClasses import book
from bookClasses import bookAd

leisureBooksCategories = [
"Laisvalaikio skaitiniai", 
"Grozine literatura", 
"Detektyvai", 
"Fantastika",
"Meiles romanai", 
"Ezoterika, parapsichologija"
]

familyHealthKidsBooksCategories = [
"Seima, sveikata, vaikams", 
"Receptai", 
"Vaikams", 
"Jaunimui",
"Teveliams"
]
documentaryBooksCategories = [
"Dokumentine literatura", 
"Atsiminimai", 
"Biografijos"
]

scientificBooksCategories = [
"Moksline literatura", 
"Zodynai, zinynai", 
"Istorija",
"Teise",
"Religija, filosofija",
"Verslas ir ekonomika",
"Psichologija, sociologija"
]

textbooksCategories = [
"Vadoveliai", 
"Lietuviu kalba", 
"Literatura",
"Matematika",
"Gamtos mokslai",
"Uzsienio kalbos",
"Istorija, politologija",
"Fizika, chemija",
"Informatika",
"Pedagogika",
"Medicina",
"Ekonomika, vadyba"
]

foreignBookCategory = "Knygos uzsienio kalbomis"

class Reading:

    def __init__(self, fileName):
        self.data = ""
        self.fileName = fileName
        self.books = ""
        self.sellers = ""
        self.bookAds = ""

    def read(self):
        with open(self.fileName, "r") as jsonFile:
            data = json.load(jsonFile)
            self.data = data

    def createObjects(self):
        books = []
        sellers = []
        bookAds = []
        with open(self.fileName, "r") as jsonFile:
            data = json.load(jsonFile)
            for ad in data:
                newBook = Reading.createBookObject(ad['title'], ad['author'], ad['releaseDate'], ad['category'])
                newSeller = seller.Seller(ad['username'], ad['city'])
                newAd = bookAd.BookAd(newBook, newSeller, ad['price'], ad['condition'], ad['username'])
                books.append(newBook)
                sellers.append(newSeller)
                bookAds.append(newAd)
        self.books = books
        self.sellers = sellers
        self.bookAds = bookAds

    @staticmethod
    def createBookObject(title, author, releaseDate, category):
        for leisureBooksCategory in leisureBooksCategories:
            if category == leisureBooksCategory:
                return leisureBook.LeisureBook(title, author, releaseDate, category)
        for familyHealthKidsBooksCategory in familyHealthKidsBooksCategories:
            if category == familyHealthKidsBooksCategory:
                return familyHealthKidsBook.FamilyHealthKidsBook(title, author, releaseDate, category)
        for documentaryBookCategory in documentaryBooksCategories:
            if category == documentaryBookCategory:
                return documentaryBook.DocumentaryBook(title, author, releaseDate, category)
        for scientificBookCategory in scientificBooksCategories:
            if category == scientificBookCategory:
                return scientificBook.ScientificBook(title, author, releaseDate, category)
        for textbooksCategory in textbooksCategories:
            if category == textbooksCategory:
                return textbook.Textbook(title, author, releaseDate, category)
        if category == foreignBookCategory:
            return foreignBook.ForeignBook(title, author, releaseDate, category)
        else:
            return otherBook.OtherBook(title, author, releaseDate, category)

    def getData(self):
        return self.data
    def getFileName(self):
        return self.fileName
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
            
    

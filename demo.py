from wrBooks import readingFromFile, writingToFile
from bookClasses import book, seller, bookAd

database = "bookAds.json"
newBooks = "bookAdsNew.json"

newDataObj = readingFromFile.Reading(newBooks)
newDataObj.read()
newDataObj.createObjects()

newBooks = newDataObj.getBooks()
newSellers = newDataObj.getSellers()
newBookAds = newDataObj.getBookAds()

databaseObj = readingFromFile.Reading(database)
databaseObj.read()

writingToFile.appendFile(databaseObj, newDataObj)

databaseObj.read()
databaseObj.createObjects()

books = databaseObj.getBooks()
sellers = databaseObj.getSellers()
bookAds = databaseObj.getBookAds()

print(str(len(newBookAds)) + " new book ads was added to file. These ads contains " +  str(book.Book.getDifferentBooksCount(newBooks)) + " different books.")
print("Now database has " + str(len(bookAds)) + " book ad was added to file. These ads contains " +  str(book.Book.getDifferentBooksCount(books)) + " different books.")
print("\n"+ "Sellers live in " + str(len(seller.Seller.getDifferentRecords(sellers, "city"))) + " differenct cities:")
for city in seller.Seller.getDifferentRecords(sellers, "city"):
   print(city)
print("\n" + "There are " + str(len(book.Book.getBooksByType(books, "Leisure books"))) + " lesure books:")
for leasureBook in book.Book.getBooksByType(books, "Leisure books"):
    print(book.Book.getTitle(leasureBook))
print("\n" + "There are " + str(len(bookAd.BookAd.getBookAdsByPrice(bookAds, "higher", 50))) + " books ads with price bigger than 50.")
print("\n" + "There are " + str(len(book.Book.getByYear(books, "equal", "2015"))) + " books written in 2015.")
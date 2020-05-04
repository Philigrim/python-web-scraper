import readingFromFile
import writingToFile
import book
import seller
import bookAd

database = "bookAds.json"
newBooks = "bookAdsNew.json"

readingObj1 = readingFromFile.Reading(newBooks)
newBookAds = readingObj1.getBookAds()
newBooks = readingObj1.getBooks()
writingToFile.Writing(database, newBookAds).save("bookads", "add")

readingObj2 = readingFromFile.Reading(database)
bookAds = readingObj2.getBookAds()
books = readingObj2.getBooks()
sellers = readingObj2.getSellers()

bookAd.BookAd.changeBookAdInfoByRecord(bookAds, "title", "Po istariant sudie", "Pries istariant sudie")
writingToFile.Writing(database, bookAds).save("bookads", "change")

print(str(len(newBookAds)) + " new book ad was added to file. These ads contains " +  str(book.Book.getDifferentBooksCount(newBooks)) + " different book.")
print("Now database has " + str(len(bookAds)) + " new book ad was added to file. These ads contains " +  str(book.Book.getDifferentBooksCount(books)) + " different books.")
print("\n"+ "Sellers live in " + str(len(seller.Seller.getDifferentRecords(sellers, "city"))) + " differenct cities:")
tempResults = []
for city in seller.Seller.getDifferentRecords(sellers, "city"):
    print(city)
print("\n" + "There are " + str(len(book.Book.getBooksByType(books, "Leisure books"))) + " lesure books:")
for leasureBook in book.Book.getBooksByType(books, "Leisure books"):
    print(book.Book.getTitle(leasureBook))
print("\n" + "There are " + str(len(bookAd.BookAd.getBookAdsByPrice(bookAds, "higher", 50))) + " books ads with price bigger than 50.")
print("There are " + str(len(book.Book.getByYear(books, "equal", "2015"))) + " books written in 2015.")
import readingFromFile
import book
import unittest

class TestBook(unittest.TestCase):

    def test_getBooksByType_leisure(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        booksList=book.Book.getBooksByType(fullBooksList, "Leisure books")
        resultList = []
        for oneBook in booksList:
            resultList.append(oneBook.getBookInfo())
        correctAnswer=[{'title': 'Tarzanas dziunglese', 'author': 'Barouzas Edgaras', 'releaseDate': '1999', 'category': 'Laisvalaikio skaitiniai'}, {'title': 'Dzeines Osten pasimatymu vadovas', 'author': 'Henderson Lauren', 'releaseDate': '2007', 'category': 'Grozine literatura'}, {'title': 'Marsietis', 'author': 'Weir Andy', 'releaseDate': '2015', 'category': 'Fantastika'}]
        self.assertEqual(resultList, correctAnswer)
        
    def test_getBooksByType_familyhealtkids(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        booksList=book.Book.getBooksByType(fullBooksList, "Family, health, kids books")
        resultList = []
        for oneBook in booksList:
            resultList.append(oneBook.getBookInfo())
        correctAnswer=[{'title': 'Anglu kelias', 'author': 'Soler Antonio', 'releaseDate': '2007', 'category': 'Jaunimui'}]
        self.assertEqual(resultList, correctAnswer)

    def test_getBooksByType_documentary(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        booksList=book.Book.getBooksByType(fullBooksList, "Documentary books")
        resultList = []
        for oneBook in booksList:
            resultList.append(oneBook.getBookInfo())
        correctAnswer=[{'title': 'Zvaigzdes', 'author': 'Harvi Ketrin', 'releaseDate': '1996', 'category': 'Biografijos'}]
        self.assertEqual(resultList, correctAnswer)

    def test_getBooksByType_scientific(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        booksList=book.Book.getBooksByType(fullBooksList, "Scientific books")
        resultList = []
        for oneBook in booksList:
            resultList.append(oneBook.getBookInfo())
        correctAnswer=[{'title': 'Nakties forma', 'author': 'Gerritsen Tess', 'releaseDate': '2019', 'category': 'Istorija'}]
        self.assertEqual(resultList, correctAnswer)

    def test_getBooksByType_textbook(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        booksList=book.Book.getBooksByType(fullBooksList, "Textbooks")
        resultList = []
        for oneBook in booksList:
            resultList.append(oneBook.getBookInfo())
        correctAnswer=[{'title': 'Saulelydis', 'author': 'Meyer Stephenie', 'releaseDate': '2009', 'category': 'Matematika'}]
        self.assertEqual(resultList, correctAnswer)

    def test_getBooksByType_foreign(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        booksList=book.Book.getBooksByType(fullBooksList, "Foreign books")
        resultList = []
        for oneBook in booksList:
            resultList.append(oneBook.getBookInfo())
        correctAnswer=[{'title': 'Pries istariant sudie', 'author': 'Clark Mary Higgins', 'releaseDate': '2015', 'category': 'Knygos uzsienio kalbomis'}]
        self.assertEqual(resultList, correctAnswer)

    def test_getBooksByType_other(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        booksList=book.Book.getBooksByType(fullBooksList, "Other books")
        resultList = []
        for oneBook in booksList:
            resultList.append(oneBook.getBookInfo())
        correctAnswer=[{'title': 'Meiles erdve', 'author': 'Megre Vladimiras', 'releaseDate': '1999', 'category': 'Ezoterika, parapsicho'}]
        self.assertEqual(resultList, correctAnswer)

if __name__ == "__main__":
    unittest.main()
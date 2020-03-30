import readingFromFile
import book
import unittest

class TestBook(unittest.TestCase):

    def test_getBooksListByRecord_title(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getBooksListByRecord(fullBooksList, "title", "Tarzanas dziunglese")
        correctAnswer = [{'title': 'Tarzanas dziunglese', 'author': 'Barouzas Edgaras', 'releaseDate': '1999', 'category': 'Laisvalaikio skaitiniai'}]
        self.assertEqual(books, correctAnswer)

    def test_getBooksListByRecord_author(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getBooksListByRecord(fullBooksList, "author", "Soler Antonio")
        correctAnswer = [{'title': 'Anglu kelias', 'author': 'Soler Antonio', 'releaseDate': '2007', 'category': 'Jaunimui'}]
        self.assertEqual(books, correctAnswer)

    def test_getBooksListByRecord_releaseDate(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getBooksListByRecord(fullBooksList, "release date", "1999")
        correctAnswer = [{'title': 'Tarzanas dziunglese', 'author': 'Barouzas Edgaras', 'releaseDate': '1999', 'category': 'Laisvalaikio skaitiniai'}, {'title': 'Meiles erdve', 'author': 'Megre Vladimiras', 'releaseDate': '1999', 'category': 'Ezoterika, parapsicho'}]
        self.assertEqual(books, correctAnswer)

    def test_getBooksListByRecord_category(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getBooksListByRecord(fullBooksList, "category", "Jaunimui")
        correctAnswer = [{'title': 'Anglu kelias', 'author': 'Soler Antonio', 'releaseDate': '2007', 'category': 'Jaunimui'}]
        self.assertEqual(books, correctAnswer)

    def test_getBooksListByRecord_etc(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getBooksListByRecord(fullBooksList, "wrong", "wrong record test")
        self.assertEqual(books, "Wrong record type")

if __name__ == "__main__":
    unittest.main()
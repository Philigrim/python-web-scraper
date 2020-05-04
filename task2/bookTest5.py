import readingFromFile
import book
import unittest

class TestBook(unittest.TestCase):

    def test_getRecordsListByRecord_title(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        titles = book.Book.getRecordsListByRecord(fullBooksList, "title")
        correctAnswer = ['Tarzanas dziunglese', 'Dzeines Osten pasimatymu vadovas', 'Anglu kelias', 'Pries istariant sudie', 'Nakties forma', 'Saulelydis', 'Marsietis', 'Zvaigzdes', 'Meiles erdve']
        self.assertEqual(titles, correctAnswer)

    def test_getRecordsListByRecord_author(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        authors = book.Book.getRecordsListByRecord(fullBooksList, "author")
        correctAnswer = ['Barouzas Edgaras', 'Henderson Lauren', 'Soler Antonio', 'Clark Mary Higgins', 'Gerritsen Tess', 'Meyer Stephenie', 'Weir Andy', 'Harvi Ketrin', 'Megre Vladimiras']
        self.assertEqual(authors, correctAnswer)

    def test_getRecordsListByRecord_releaseDate(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        relDates = book.Book.getRecordsListByRecord(fullBooksList, "release date")
        correctAnswer = ['1999', '2007', '2007', '2015', '2019', '2009', '2015', '1996', '1999']
        self.assertEqual(relDates, correctAnswer)

    def test_getRecordsListByRecord_category(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        categories = book.Book.getRecordsListByRecord(fullBooksList, "category")
        correctAnswer = ['Laisvalaikio skaitiniai', 'Grozine literatura', 'Jaunimui', 'Knygos uzsienio kalbomis', 'Istorija', 'Matematika', 'Fantastika', 'Biografijos', 'Ezoterika, parapsicho']
        self.assertEqual(categories, correctAnswer)

    def test_getRecordsListByRecord_etc(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        wrong = book.Book.getRecordsListByRecord(fullBooksList, "wrong input")
        self.assertEqual(wrong, "Wrong record type")

if __name__ == "__main__":
    unittest.main()
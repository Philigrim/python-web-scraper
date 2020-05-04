import readingFromFile
import book
import unittest

class TestBook(unittest.TestCase):

    def test_getIdenticalRecordsCountByRecord_title(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getIdenticalRecordsCountByRecord(fullBooksList, "title", "Tarzanas dziunglese"), 1)

    def test_getIdenticalRecordsCountByRecord_author(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getIdenticalRecordsCountByRecord(fullBooksList, "author", "Henderson Lauren"), 1)

    def test_getIdenticalRecordsCountByRecord_releaseDate(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getIdenticalRecordsCountByRecord(fullBooksList, "release date", "2015"), 2)

    def test_getIdenticalRecordsCountByRecord_category(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getIdenticalRecordsCountByRecord(fullBooksList, "category", "Vaikams"), 0)

    def test_getIdenticalRecordsCountByRecord_type(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getIdenticalRecordsCountByRecord(fullBooksList, "type", "Leisure books"), 3)

    def test_getIdenticalRecordsCountByRecord_etc(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getIdenticalRecordsCountByRecord(fullBooksList, "wrong input", "Hello"), "Wrong record type")

if __name__ == "__main__":
    unittest.main()
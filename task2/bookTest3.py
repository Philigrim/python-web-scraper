import readingFromFile
import book
import unittest

class TestBook(unittest.TestCase):

    def test_getDifferentRecordsCountByRecord_title(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getDifferentRecordsCountByRecord(fullBooksList, "title"), 9)

    def test_getDifferentRecordsCountByRecord_author(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getDifferentRecordsCountByRecord(fullBooksList, "author"), 9)

    def test_getDifferentRecordsCountByRecord_releaseDate(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getDifferentRecordsCountByRecord(fullBooksList, "release date"), 9)

    def test_getDifferentRecordsCountByRecord_category(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getDifferentRecordsCountByRecord(fullBooksList, "category"), 9)

    def test_getDifferentRecordsCountByRecord_type(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getDifferentRecordsCountByRecord(fullBooksList, "type"), 9)

    def test_getDifferentRecordsCountByRecord_etc(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        self.assertEqual(book.Book.getDifferentRecordsCountByRecord(fullBooksList, "wrong input"), "Wrong record type")

if __name__ == "__main__":
    unittest.main()
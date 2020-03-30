import readingFromFile
import book
import unittest

class TestBook(unittest.TestCase):

    def test_getBookType_leisure(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        book = fullBooksList[0]
        self.assertEqual(book.getBookType(), "Leisure books")

    def test_getBookType_familyhealtkids(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        book = fullBooksList[2]
        self.assertEqual(book.getBookType(), "Family, health, kids books")
        
    def test_getBookType_documentary(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        book = fullBooksList[7]
        self.assertEqual(book.getBookType(), "Documentary books")

    def test_getBookType_scientific(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        book = fullBooksList[4]
        self.assertEqual(book.getBookType(), "Scientific books")

    def test_getBookType_textbook(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        book = fullBooksList[5]
        self.assertEqual(book.getBookType(), "Textbooks")
        
    def test_getBookType_foreign(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        book = fullBooksList[3]
        self.assertEqual(book.getBookType(), "Foreign books")

    def test_getBookType_other(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        book = fullBooksList[8]
        self.assertEqual(book.getBookType(), "Other books")
        
if __name__ == "__main__":
    unittest.main()
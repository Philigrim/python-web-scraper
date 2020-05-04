import readingFromFile
import book
import unittest

class TestBook(unittest.TestCase):
    
    def test_getByYear_older(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getByYear(fullBooksList, "older", "2000")
        resultList = []
        for oneBook in books:
            resultList.append(oneBook.getBookInfo())
        correctAnswer = [{'title': 'Tarzanas dziunglese', 'author': 'Barouzas Edgaras', 'releaseDate': '1999', 'category': 'Laisvalaikio skaitiniai'}, {'title': 'Zvaigzdes', 'author': 'Harvi Ketrin', 'releaseDate': '1996', 'category': 'Biografijos'}, {'title': 'Meiles erdve', 'author': 'Megre Vladimiras', 'releaseDate': '1999', 'category': 'Ezoterika, parapsicho'}, {'title': 'Kaip issigyditi paciam', 'author': 'Malovicka Anatolijus', 'releaseDate': '1993', 'category': 'Ezoterika, parapsichologija'}, {'title': 'Kaip issigyditi paciam', 'author': 'Malovicka Anatolijus', 'releaseDate': '1993', 'category': 'Ezoterika, parapsichologija'}]
        self.assertEqual(resultList, correctAnswer)

    def test_getByYear_newer(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getByYear(fullBooksList, "newer", "2000")
        resultList = []
        for oneBook in books:
            resultList.append(oneBook.getBookInfo())
        correctAnswer = [{'title': 'Dzeines Osten pasimatymu vadovas', 'author': 'Henderson Lauren', 'releaseDate': '2007', 'category': 'Grozine literatura'}, {'title': 'Anglu kelias', 'author': 'Soler Antonio', 'releaseDate': '2007', 'category': 'Jaunimui'}, {'title': 'Pries istariant sudie', 'author': 'Clark Mary Higgins', 'releaseDate': '2015', 'category': 'Knygos uzsienio kalbomis'}, {'title': 'Nakties forma', 'author': 'Gerritsen Tess', 'releaseDate': '2019', 'category': 'Istorija'}, {'title': 'Saulelydis', 'author': 'Meyer Stephenie', 'releaseDate': '2009', 'category': 'Matematika'}, {'title': 'Marsietis', 'author': 'Weir Andy', 'releaseDate': '2015', 'category': 'Fantastika'}]
        self.assertEqual(resultList, correctAnswer)

    def test_getByYear_equal(self):
        fullBooksList = readingFromFile.Reading("bookAds.json").getBooks()
        books = book.Book.getByYear(fullBooksList, "equal", "2000")
        resultList = []
        for oneBook in books:
            resultList.append(oneBook.getBookInfo())
        self.assertEqual(resultList, [])

if __name__ == "__main__":
    unittest.main()
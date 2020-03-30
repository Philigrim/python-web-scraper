import readingFromFile
import seller
import unittest

class TestBook(unittest.TestCase):
    
    def test_getSellerCountByCity_Vilnius(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getSellerCountByCity(fullSellersList, 'Vilnius'), 1)

    def test_getSellerCountByCity_Kaunas(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getSellerCountByCity(fullSellersList, 'Kaunas'), 2)

    def  test_getSellerCountByCity_Klaipeda(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getSellerCountByCity(fullSellersList, 'Klaipeda'), 1)

if __name__ == "__main__":
    unittest.main()
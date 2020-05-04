import readingFromFile
import seller
import unittest

class TestBook(unittest.TestCase):
    
    def test_getSellerUsernamesByCity_Vilnius(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getSellerUsernamesByCity(fullSellersList, "Vilnius"), ['philigrim'])

    def test_getSellerUsernamesByCity_Kaunas(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getSellerUsernamesByCity(fullSellersList, "Kaunas"), ['bookmagnat', 'kaunaz123'])

    def test_getSellerUsernamesByCity_Klaipeda(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getSellerUsernamesByCity(fullSellersList, "Klaipeda"), ['klaipedietis'])

if __name__ == "__main__":
    unittest.main()
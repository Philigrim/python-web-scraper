import readingFromFile
import seller
import unittest

class TestBook(unittest.TestCase):
    
    def test_getDifferentRecords_city(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getDifferentRecords(fullSellersList, "city"), {'klaipeda', 'vilnius', 'kaunas', 'plunge'})
        
    def test_getDifferentRecords_username(self):
        fullSellersList = readingFromFile.Reading("bookAds.json").getSellers()
        self.assertEqual(seller.Seller.getDifferentRecords(fullSellersList, "username"), {'klaipedietis', 'admin', 'kaunaz123', 'unknow', 'phil', 'bookmagnat', 'philigrim'})

if __name__ == "__main__":
    unittest.main()
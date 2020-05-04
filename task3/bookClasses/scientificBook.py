from bookClasses.book import Book

class ScientificBook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)    
      
    @staticmethod
    def isScientificBook(category):
        scientificBooksCategories = [
            "Moksline literatura", 
            "Zodynai, zinynai", 
            "Istorija",
            "Teise",
            "Religija, filosofija",
            "Verslas ir ekonomika",
            "Psichologija, sociologija"
            ]
        for scientificBookCategory in scientificBooksCategories:
            if scientificBookCategory == category:
                return True
        return False

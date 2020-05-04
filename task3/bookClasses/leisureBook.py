from bookClasses.book import Book

class LeisureBook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)    
    
    @staticmethod
    def isLeisureBook(category):
        leisureBooksCategories = [
            "Laisvalaikio skaitiniai", 
            "Grozine literatura", 
            "Detektyvai", 
            "Fantastika",
            "Meiles romanai", 
            "Ezoterika, parapsichologija"
            ]
        for leisureBookCategory in leisureBooksCategories:
            if leisureBookCategory == category:
                return True
        return False

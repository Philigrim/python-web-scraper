from bookClasses.book import Book

class Textbook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)  
      
    @staticmethod
    def isTextbook(category):
        textbooksCategories = [
            "Vadoveliai", 
            "Lietuviu kalba", 
            "Literatura",
            "Matematika",
            "Gamtos mokslai",
            "Uzsienio kalbos",
            "Istorija, politologija",
            "Fizika, chemija",
            "Informatika",
            "Pedagogika",
            "Medicina",
            "Ekonomika, vadyba"
            ]
        for textbookCategory in textbooksCategories:
            if textbookCategory == category:
                return True
        return False

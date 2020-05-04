from bookClasses.book import Book

class ForeignBook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)        
      
    @staticmethod
    def isForeignBook(category):
        foreignBookCategory = "Knygos uzsienio kalbomis"
        if foreignBookCategory == category:
            return True
        return False

from bookClasses.book import Book

class DocumentaryBook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)    

    @staticmethod
    def isDocumentaryBook(category):
        DocumentaryBooksCategories = [
            "Dokumentine literatura", 
            "Atsiminimai", 
            "Biografijos"
            ]
        for documentaryBookCategory in DocumentaryBooksCategories:
            if documentaryBookCategory == category:
                return True
        return False

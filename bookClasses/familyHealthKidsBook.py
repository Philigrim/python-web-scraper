from bookClasses.book import Book

class FamilyHealthKidsBook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)    

    @staticmethod
    def isFamilyHealthKidsBook(category):
        FamilyHealthKidsBooksCategories = [
            "Seima, sveikata, vaikams", 
            "Receptai", 
            "Vaikams", 
            "Jaunimui",
            "Teveliams"
            ]
        for familyHealthKidsBookCategory in FamilyHealthKidsBooksCategories:
            if familyHealthKidsBookCategory == category:
                return True
        return False

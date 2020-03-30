class Book:
    title = ""
    author = ""
    releaseDate = ""
    category = ""

    def __init__(self, title, author, releaseDate, category):
        self.title = title
        self.author = author
        self.releaseDate = releaseDate
        self.category = category

    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getReleaseDate(self):
        return self.releaseDate
    def getCategory(self):
        return self.category
    def getBookInfo(self):
        return {
            'title' : self.title,
            'author' : self.author, 
            'releaseDate' : self.releaseDate,
            'category' : self.category}

    def changeTitle(self, title):
        self.title = title
    def changeAuthor(self, author):
        self.author = author
    def changeReleaseDate(self, releaseDate):
        self.releaseDate = releaseDate
    def changeCategory(self, category):
        self.category = category
    def changeBookInfo(self, title, author, releaseDate, category):
        self.title = title
        self.author = author
        self.releaseDate = releaseDate
        self.category = category

    @staticmethod
    def createBookObject(title, author, releaseDate, category):
        if LeisureBook.isLeisureBook(category):
            return LeisureBook(title, author, releaseDate, category)
        elif FamilyHealthKidsBook.isFamilyHealthKidsBook(category):
            return FamilyHealthKidsBook(title, author, releaseDate, category)
        elif DocumentaryBook.isDocumentaryBook(category):
            return DocumentaryBook(title, author, releaseDate, category)
        elif ScientificBook.isScientificBook(category):
            return ScientificBook(title, author, releaseDate, category)
        elif Textbook.isTextbook(category):
            return Textbook(title, author, releaseDate, category)
        elif ForeignBook.isForeignBook(category):
            return ForeignBook(title, author, releaseDate, category)
        else:
            return OtherBook(title, author, releaseDate, category)

    @staticmethod
    def getBooksByType(books, genre):
        booksByGenre = []
        for book in books:
            if book.getBookType()==genre:
                booksByGenre.append(book)
        return booksByGenre

    def getBookType(self):
        bookType=str(type(self))
        if bookType == ("<class 'book.LeisureBook'>"):
            return ("Leisure books")
        elif bookType == ("<class 'book.FamilyHealthKidsBook'>"):
            return ("Family, health, kids books")
        elif bookType == ("<class 'book.DocumentaryBook'>"):
            return ("Documentary books")
        elif bookType == ("<class 'book.ScientificBook'>"):
            return ("Scientific books")
        elif bookType == ("<class 'book.Textbook'>"):
            return ("Textbooks")
        elif bookType == ("<class 'book.ForeignBook'>"):
            return ("Foreign books")
        else:
            return ("Other books")
        
    @staticmethod 
    def getDifferentBooksCount(books):
        diffBooks = []
        for book in books:
            oneBookSet = []
            oneBookSet.append(book.getTitle())
            oneBookSet.append(book.getAuthor())
            diffBooks.append(oneBookSet)
        return len(dict(diffBooks))

    @staticmethod 
    def getDifferentRecordsCountByRecord(books, record):
        records = []
        if record.lower() == "title":
            for book in books:
                records.append(book.getTitle())
        elif record.lower() == "author":
            for book in books:
                records.append(book.getAuthor())
        elif record.lower() == "release date":
            for book in books:
                records.append(book.getAuthor())
        elif record.lower() == "category":
            for book in books:
                records.append(book.getAuthor())
        elif record.lower() == "type" or record.lower() == "genre":
            for book in books:
                records.append(book.getBookType())
        else:
            return "Wrong record type"
        return len(records)

    @staticmethod 
    def getIdenticalRecordsCountByRecord(books, record, value):
        count = 0
        if record.lower() == "title":
            for book in books:
                if book.getTitle().lower() == value.lower():
                    count += 1
        elif record.lower() == "author":
            for book in books:
                if book.getAuthor().lower() == value.lower():
                    count += 1
        elif record.lower() == "release date":
            for book in books:
                if book.getReleaseDate() == value:
                    count += 1
        elif record.lower() == "category":
            for book in books:
                if book.getCategory().lower() == value.lower():
                    count += 1
        elif record.lower() == "type" or record.lower() == "genre":
            for book in books:
                if book.getBookType().lower() == value.lower():
                    count += 1
        else:
            return "Wrong record type"
        return count

    @staticmethod
    def getRecordsListByRecord(books, record):
        recordsList=[]
        if record.lower() == "title":
            for book in books:
                recordsList.append(book.getTitle())
        elif record.lower() == "author":
            for book in books:
                recordsList.append(book.getAuthor())
        elif record.lower() == "release date":
            for book in books:
                recordsList.append(book.getReleaseDate())
        elif record.lower() == "category":
            for book in books:
                recordsList.append(book.getCategory())
        else:
            return "Wrong record type"
        return recordsList

    @staticmethod 
    def getBooksListByRecord(books, record, value):
        booksByRecord=[]
        if record.lower() == "title":
            for book in books:
                if book.getTitle().lower() == value.lower():
                    booksByRecord.append(book.getBookInfo())
        elif record.lower() == "author":
            for book in books:
                if book.getAuthor().lower() == value.lower():
                    booksByRecord.append(book.getBookInfo())
        elif record.lower() == "release date":
            for book in books:
                if book.getReleaseDate() == value.lower():
                    booksByRecord.append(book.getBookInfo())
        elif record.lower() == "category":
            for book in books:
                if book.getCategory().lower() == value.lower():
                    booksByRecord.append(book.getBookInfo())
        else:
            return "Wrong record type"
        return booksByRecord

    @staticmethod
    def getByYear(books, choice, year):
        booksList = []
        if choice.lower() == "older" :
            for book in books:
                if int(book.getReleaseDate())<int(year):
                    booksList.append(book)
        elif choice.lower() == "newer" :
            for book in books:
                if int(book.getReleaseDate())>int(year):
                    booksList.append(book)
        elif choice.lower() == "equal" :
            for book in books:
                if int(book.getReleaseDate())==int(year):
                    booksList.append(book)
        else:
            return "Wrong choice selected."
        return booksList

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

class ForeignBook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)    
      
    @staticmethod
    def isForeignBook(category):
        foreignBookCategory = "Knygos uzsienio kalbomis"
        if foreignBookCategory == category:
            return True
        return False
    
class OtherBook(Book):       
    def __init__(self, title, author, releaseDate, category):
        super().__init__(title, author, releaseDate, category)
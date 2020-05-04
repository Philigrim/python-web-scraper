class Book:

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
    def getBooksByType(books, genre):
        booksByGenre = []
        for book in books:
            if book.getBookType()==genre:
                booksByGenre.append(book)
        return booksByGenre

    def getBookType(self):
        bookType=str(type(self))
        if bookType == ("<class 'bookClasses.leisureBook.LeisureBook'>"):
            return ("Leisure books")
        elif bookType == ("<class 'bookClasses.familyHealthKidsBook.FamilyHealthKidsBook'>"):
            return ("Family, health, kids books")
        elif bookType == ("<class 'bookClasses.documentaryBook.DocumentaryBook'>"):
            return ("Documentary books")
        elif bookType == ("<class 'bookClasses.scientificBook.ScientificBook'>"):
            return ("Scientific books")
        elif bookType == ("<class 'bookClasses.textbook.Textbook'>"):
            return ("Textbooks")
        elif bookType == ("<class 'bookClasses.foreignBook.ForeignBook'>"):
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

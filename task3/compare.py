#import runWebScraper
import time
import webScraper
from threading import Thread

def runTest(url, newBooksFile, categoriesWanted, booksWantedFromOneCategory, isMultiThread):
    start = time.perf_counter()
    webScraper.runScrape(url, newBooksFile, categoriesWanted, booksWantedFromOneCategory, isMultiThread)
    finish = time.perf_counter()
    if isMultiThread:
        print(f'Multiple threaded: {round(finish-start,2)} second(s)')
    else:
        print(f'Single threaded: {round(finish-start,2)} second(s)')

if __name__ == "__main__":
        # url - is kokio puslapio bus scrapinama
    url = "https://www.sena.lt"
    # newBooksFile - failo pavadinimas, i kuri bus surasyti knygu duomenys
    newBooksFile = "bookAdsNew.json"
    # categoriesWanted - is kiek kategoriju norima scrapint 1-37
    categoriesWanted = 10
    # booksWantedFromOneCategory - kiek norima knygu is vienos kategorijos 1-24
    booksWantedFromOneCategory = 5

    t1 = Thread(target=runTest, args=(url, newBooksFile, categoriesWanted, booksWantedFromOneCategory, True,))
    t1.start()

    t2 = Thread(target=runTest, args=(url, newBooksFile, categoriesWanted, booksWantedFromOneCategory, False,))
    t2.start()
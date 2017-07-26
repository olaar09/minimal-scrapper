import sys
import scapper
import multiprocessing

output = multiprocessing.Queue()

class minimal:

    def __init__(self):
        sys.stdout.write('Starting minimal scrapper \n')

    def startScapper(self, url):
        sys.stdout.write('Getting contents of  url :')
        scrape = scapper.ScrapeUrl(url)

        sys.stdout.write( url+ '\n')
        scrape.getSource()

        sys.stdout.write("Scrapping emails from content \n")
        out = scrape.scrapeEmails().__str__()
        if len(out) > 2:
            scrape.saveData(out)
        return



if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stdout.write('Could not start program, expected "minimal.py <url>" \n')
        sys.exit()

    minimalScraper = minimal()
    for url in  sys.argv[1:]:
        multiprocessing.Process(target=minimalScraper.startScapper(url)).start()
        print("Started thread for {} ".format(url))



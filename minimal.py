import sys
import scapper

class minimal:

    def __init__(self, args):
        sys.stdout.write('Starting minimal scrapper \n')
        if len(args) < 2:
            sys.stdout.write('Could not start program, expected "minimal.py <url>" \n')
            sys.exit()
        else:
            self.args = args

    def startScapper(self):
        sys.stdout.write('Getting contents of  url :')
        scrape = scapper.ScrapeUrl(self.args[1])

        sys.stdout.write( self.args[1]+ '\n')
        scrape.getSource()

        sys.stdout.write("Scrapping emails from content \n")
        return scrape.scrapeEmails()




if __name__ == '__main__':
    minimalScraper = minimal(sys.argv)
    print(minimalScraper.startScapper())

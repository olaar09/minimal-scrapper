import urllib.request as request
import re

class ScrapeUrl:

    def __init__(self, url):
        self.__url = url
        self.__htmlContent = ""


    def getSource(self):
        respons =  request.urlopen(self.__url)
        self.__htmlContent =  respons.read().decode('utf-8')



    def scrapeEmails(self):
        return re.findall(r'[\w\.-]+@[\w\.-]+', self.__htmlContent)

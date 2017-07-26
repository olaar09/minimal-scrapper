import urllib.request as request, urllib.error as reqErr
import sys
import re
import time

class ScrapeUrl:

    def __init__(self, url):
        self.__url = url
        self.__htmlContent = ""


    def getSource(self):
        headers = {}
        headers[
            'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = request.Request(self.__url, headers=headers)
        try:
            resp = request.urlopen(req)
            self.__htmlContent = resp.read().decode('utf-8')
        except  reqErr.URLError as e: sys.stderr.write("Error reading url "+self.__url+ " Trace: "+ e.reason);



    def scrapeEmails(self):
        return re.findall(r'[\w\.-]+@[\w\.-]+', self.__htmlContent)


    def saveData(self, data):
        with open("data/{}{}".format(str(time.time()), ".txt"), "w") as file:
            file.write(data)


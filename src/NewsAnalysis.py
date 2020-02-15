import requests

from textblob import TextBlob
from bs4 import BeautifulSoup


class Analysis:
    def __init__(self, term):
        term = term.replace(" ", "+")
        self.term = term
        self.subjectivity = 0
        self.sentiment = 0

        self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(
            self.term)

    def run(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # getting the tag with all the headlines
        headline_results = soup.find_all('div', class_='BNeawe')
        #print(headline_results)
        for h in headline_results:
            blob = TextBlob(h.get_text())
            self.sentiment += blob.sentiment.polarity/len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity / \
                len(headline_results)


def newsAnalysor(queryName):
    a = Analysis(queryName)
    a.run()
    newsAnalysis = a.sentiment*a.subjectivity*10
    return newsAnalysis

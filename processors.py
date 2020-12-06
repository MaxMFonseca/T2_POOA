from abc import ABC, abstractmethod
from pathlib import Path
import csv

class Processor(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass

## EXPORT NEWS AS CSV ##
class ExportNewsAsCsv(Processor):
    def __init__(self, siteName, news):
        self.siteName = siteName
        self.news = news

    def execute(self):
        Path("output/csv/").mkdir(parents=True, exist_ok=True)
        with open("output/csv/" + self.siteName + ".csv", 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(["title", "url"])
            for title, url in self.news:
                writer.writerow([title,url])

## GET LETTER APEARING FREQUENCY ( param letters = "Caracteres à procurar por") ##
class GetLetterApearingFrequency(Processor):
    def __init__(self, siteName, news):
        self.siteName = siteName
        self.news = news
    
    def execute(self, letters):
        lFreq = []

        for i in range(len(letters)):
            lFreq.append(0)

        for name, disc in self.news:
            for c in name:
                for i in range(len(letters)):
                    if c == letters[i]:
                        lFreq[i] += 1

        for i in range(len(letters)):
            print(f"Letter {letters[i]} appears {lFreq[i]} times.")

## FILTER BY WORD ( param words = "Palavras à procurar por") ##
class FilterByWord(Processor):
    def __init__(self, siteName, news):
        self.siteName = siteName
        self.news = news

    def execute(self, words):
        print("     ** " + self.siteName.upper() + " **\n")
        for word in words:
            word = word.lower()
            print("  * " + word.upper() + " *\n")
            for name, url in self.news:
                if word in name.lower():
                    print(name)
                    print(url)
                    print('\n')
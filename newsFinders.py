from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class NewsFinder(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getData(self):
        pass  

## ESTADAO ##
class EstadaoFinder(NewsFinder):
	def __init__(self):
		self.name = 'Estadão'
		self.url = 'https://www.estadao.com.br/'
		
	def getData(self):
		html_text = requests.get(self.url).content
		soup = BeautifulSoup(html_text, 'html.parser')
		data = []

		sFind = soup.find_all('div', class_="intro")
		for s in sFind:
			url = s.find('a')['href']
			title = s.find('a')['title']
			data.append((title,url))
		
		return data

## TERRA ##
class TerraFinder(NewsFinder):
	def __init__(self):
		self.name = 'Terra'
		self.url = 'https://www.terra.com.br/noticias/'
		
	def getData(self):
		html_text = requests.get(self.url).content
		soup = BeautifulSoup(html_text, 'html.parser')
		data = []

		sFind = soup.find_all('div', class_="title")
		for s in sFind:
			url = s.find('a')['href']
			title = s.find('a').get_text()
			data.append((title,url))
		
		return data

## GLOBO NOTICIAS ##
class OGloboFinder(NewsFinder):
	def __init__(self):
		self.name = 'O Globo Notícias'
		self.url = 'https://oglobo.globo.com/'
		
	def getData(self):
		html_text = requests.get(self.url).content
		soup = BeautifulSoup(html_text, 'html.parser')
		data = []

		sFind = soup.find_all('h1', class_='teaser__title')
		for s in sFind:
			url = s.find('a')['href']
			title = s.find('a').get_text()
			data.append((title,url))
		
		return data

## UOL NOTICIAS ##
class UolFinder(NewsFinder):
    def __init__(self):
        self.name = 'UOL Notícias'
        self.url = 'https://noticias.uol.com.br/'

    def getData(self):
        html_text = requests.get(self.url).content
        soup = BeautifulSoup(html_text, 'html.parser')
        data = []
            
        sFind = soup.find_all('div', class_='thumbnails-wrapper')   
        for s in sFind:
            url = s.find('a')['href']
            title = s.find('h3').get_text() 
            data.append((title,url))  
            
        return data
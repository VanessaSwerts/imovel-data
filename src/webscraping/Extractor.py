from bs4 import BeautifulSoup
from selenium import webdriver
import os

class Extractor():

  # Define chrome driver to use selenium
  def getChromeDriver(self):
    chromedriver = f'{os.getcwd()}/src/webscraping/driver/chromedriver.exe'
    os.environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(chromedriver)

  # Get a page content passing page url using BeatifulSoup
  # page: url of the page that will be find
  def getPageContent(self, page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup

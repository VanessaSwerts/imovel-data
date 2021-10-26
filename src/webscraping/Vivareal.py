from Property import Property
from Extractor import Extractor
import time
import pandas as pd
import os

class Vivareal():
  # Get all properties in one specfic page
  # pageContet: page content found
  def getPageProperties(self, pageContent):
    cardProperties = pageContent.findAll('article', attrs={'class': 'property-card__container js-property-card'})
    
    properties = []

    for card in cardProperties:
      property = Property(card).extractPropertyInfo()
      properties.append(property)  
      print(property)      

    print(f'{len(properties)} properties found')

    return properties

  # Get all properties from vivareal by city
  # city: city to be filter in url 
  def getPropertiesByCity(self, city):
    print(f'getting all properties from {city}')

    pageUrl = f'https://www.vivareal.com.br/venda/minas-gerais/{city}'
    finalPage = False
    pageNumber = 1
    allCityProperties = []
    
    webDriver = Extractor().getChromeDriver()
    webDriver.get(pageUrl)

    while(finalPage == False):
      print(f'getting from page {pageNumber}')

      time.sleep(5)

      page = webDriver.execute_script("return document.body.innerHTML")
      pageContent = Extractor().getPageContent(page)

      allCityProperties.extend(self.getPageProperties(pageContent))

      nextPageButton = pageContent.find('a', attrs={'title': 'Próxima página'})
      if(nextPageButton != None and nextPageButton['href'].split('=')[-1] != ''):
        nextPageButtonSelenium = webDriver.find_element_by_xpath("//a[@title='Próxima página']")
        webDriver.execute_script("arguments[0].click()", nextPageButtonSelenium)
      else:
        finalPage = True

      pageNumber = pageNumber + 1

    webDriver.quit()

    return allCityProperties 

  # Transform data to dataframe and save as csv
  def saveData(self, data, fileName):
    print("Saving as csv...")
    df = pd.DataFrame(data)
    df.to_csv(f'{os.getcwd()}/src/datasets/{fileName}', index = False, header=True)
    print("Done")

  # Get all properties from vivareal website
  # cities: array that contains all cities to get the properties
  def getAllProperties(self, cities, fileName):
    properties = []

    for city in cities:
      properties.extend(self.getPropertiesByCity(city))
      self.saveData(properties, fileName)

    return properties
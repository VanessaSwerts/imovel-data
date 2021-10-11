class Property():
  
  # Constructor
  # propertyCard: card of the property that contains all the necessary information about the property
  def __init__(self, propertyCard):
    self.propertyCard = propertyCard

  # Remove initial and final spaces from a string
  # str: string to remove the spaces
  def trimStr(self, str):
    return str.rstrip().lstrip()

  # Method to get property id
  def getId(self):
    id = self.propertyCard.parent['id'] if self.propertyCard.parent.has_attr('id') else self.propertyCard.parent.parent['id'] 
    return id

  # Method to get property type
  def getType(self):
    type = self.propertyCard.find('h2', attrs={'class': 'property-card__header'}).span
    return self.trimStr(type.text.split()[0]) if type != None else "--"

  # Method to get property location
  def getLocation(self):
    location = self.propertyCard.find('span', attrs={'class': 'property-card__address'})
    return self.trimStr(location.text.split(',')[-1]) if location != None else "--"

  # Method to get property area
  def getArea(self):
    area = self.propertyCard.find('li', attrs={'class': 'property-card__detail-area'}).span
    return self.trimStr(area.text) if area != None else "--"

  # Method to get property bedrooms
  def getBedrooms(self):
    bedroom = self.propertyCard.find('li', attrs={'class': 'property-card__detail-room'}).span
    return self.trimStr(bedroom.text) if bedroom != None else "--"

  # Method to get property bathrooms
  def getBathrooms(self):
    bathroom = self.propertyCard.find('li', attrs={'class': 'property-card__detail-bathroom'}).span
    return self.trimStr(bathroom.text) if bathroom != None else "--"

  # Method to get property garage
  def getGarage(self):
    garage = self.propertyCard.find('li', attrs={'class': 'property-card__detail-garage'}).span
    return self.trimStr(garage.text) if garage != None else "--"

  # Method to get property condominium value
  def getCondominium(self):
    condominium = self.propertyCard.find('strong', attrs={'class': 'js-condo-price'})
    return self.trimStr(condominium.text) if condominium != None else "--"

  # Method to get property price
  def getPrice(self):
    price = self.propertyCard.find('div', attrs={'class': 'property-card__price'}).p
    return self.trimStr(price.text) if price != None else "--"

  # Extract information about each property
  def extractPropertyInfo(self):
    return {
      'id': self.getId(),
      'type': self.getType(),
      'location': self.getLocation(),
      'area': self.getArea(),
      'bedroom': self.getBedrooms(),
      'bathroom': self.getBathrooms(),
      'garage': self.getGarage(),
      'condominium': self.getCondominium(),
      'price': self.getPrice()  
    }
class ObjectToNumber():
    """
    This class converts property numeric object type to number.
    """
    def __init__(self, df):
        self.df = df

    def areaToNumber(self):
        """
        This function converts the area of a property to a number.
        """
        newArea = self.df['area'].str.split("-", n=1, expand=True)
        return newArea[0].astype(float)

    def bedroomToNumber(self):
        """
        This function converts the bedrooms of a property to a number.
        """
        newBedroom = self.df['bedroom'].str.split("-", n=1, expand=True)
        return newBedroom[0].astype(float)

    def bathroomToNumber(self):
        """
        This function converts the bathrooms of a property to a number.
        """
        newBathroom = self.df['bathroom'].str.split("-", n=1, expand=True)
        return newBathroom[0].astype(float)

    def garageToNumber(self):
        """
        This function converts the garages of a property to a number.
        """
        newGarage = self.df['garage'].str.split("-", n=1, expand=True)
        return newGarage[0].astype(float)

    def condominiumToNumber(self):
        """
        This function converts the condominium value of a property to a number.
        """
        newCondominium = self.df['condominium'].str.replace('[^0-9]', '', regex=True)
        return newCondominium.astype(float)

    def priceToNumber(self):
        """
        This function converts the price of a property to a number.
        """ 
        newPrice = self.df['price'].str.replace('[^0-9]', '', regex=True)
        return newPrice.astype(float)
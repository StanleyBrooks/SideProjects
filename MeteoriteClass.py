"""class Meteorite:

    def __init__(self, name, meteoid, nametype, recclass, mass, fall, year, reclat, reclong, GeoLocation):
        self.__name = name
        self.__meteoid = meteoid
        self.__nametype = nametype
        self.__recclass = recclass
        self.__mass = mass
        self.__fall = fall
        self.__year = year
        self.__reclat = reclat
        self.__reclong = reclong
        self.__GeoLocation = GeoLocation

    def to_string(self):
        return "{} was a meteorite with a mass of {}(kg) that landed in {} with a latitude of: {}, longitude of: {}, and a GeoLocation of {}".format(self.__name, self.__mass, self.__year, self.__reclat, self.__reclong, self.__GeoLocation)
"""

class Meteorite:

    """A simple meteorite class"""
    def createName(self, name):
        self.name = name
    def displayName(self):
        return self.name
    def to_string(self):
        return "{} was a meteorite".format(self.name)

first = Meteorite()
first.createName('meteo')
first.displayName()
first.to_string()
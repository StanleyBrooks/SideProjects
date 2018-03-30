import pandas as pd

def read_csv_with_pandas():
    file = 'Meteorite_Landings.csv'

    DATATYPES = {'name': str,
                'id': int,
                'nametype': str,
                'recclass': str,
                'mass': float,
                'fall': str,
                'year': int,
                'reclat': float,
                'reclong': float,
                'GeoLocation': str}

    NA=['N/A','null', '0', 'NaN', 'NaT']

    meteorites = pd.read_csv(file,
                    dtype=DATATYPES,
                    na_values=NA,
                    encoding="utf-8")

    #This converts the year column from a string into a datetime datatype
    #coerce sets all invalid dates to NaN
    meteorites['year'] = pd.to_datetime(meteorites['year'], errors='coerce')

    #Drop Null Values
    meteorites = meteorites.dropna()

    #converting mass from grams to kilograms
    meteorites['mass_kg'] = (meteorites['mass']/1000)

    #Extract the year only out of year column
    meteorites['year_only']=meteorites.year.map(lambda x: x.strftime('%Y'))

    #sort the data into useful columns
    meteorites = meteorites[['name', 'mass_kg', 'year_only', 'reclat', 'reclong', 'GeoLocation']]
    return meteorites
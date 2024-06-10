class Band:
    all =[]  # list of all instances of Band
    def __init__(self, name, hometown):
        #Initialize a Band instance with a name and hometown
        #RaisesValueError: if hometown is not a non-empty string

        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("Hometown must be a non-empty string")
        self.name = name
        Band.all.append(self)  # add self to all instances

    @property
    def name(self):
        """
        Getter for the name of the band
        """
        return self._name
    # name setter that ensures the name is a non_empty string
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("Name must be non-empty string")
    
    @property
    def hometown(self):
        #Getter for the hometown of the band
        return self._hometown 

    def concerts(self):
        # get all concerts where the band is performing
        concerts = [concert for concert in Concert.all if concert.band == self]
        return concerts if concerts else None

    def venues(self):
        #Get all venues where the band has performed
        venues = list(set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    def play_in_venue(self, venue, date):
        #Create a new concert for the band at the given venue on the given date
        #Venue has to be an instance of the Venue class
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        return Concert(date, self, venue)

    def all_introductions(self):
        """
        Get the introductions for all concerts where the band is performing
        """
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    all = []  # list of all instances of Concert
    def __init__(self, date, band, venue):
        #Initialize a Concert instance with a date, band, and venue
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)  # add self to all instances

    @property
    def date(self):
        #Getter for the date of the concert
        return self._date
    
    @date.setter
    def date(self, date):
        #Setter for the date of the concert
        #Date must be a non-empty string
        if isinstance(date, str) and len(date):
            self._date = date
        else:
            raise ValueError("Date must be non-empty string")
        
    @property
    def band(self):
        #Getter for the band performing at the concert
        
        return self._band
    @band.setter
    def band(self, band):
        #Setter for the band performing at the concert
        #Band must be of type Band        
        if not isinstance(band, Band):
            raise TypeError("Band must be of type Band")
        self._band = band

    @property
    def venue(self):
        #Getter for the venue where the concert will be held
        return self._venue
    @venue.setter
    def venue(self, venue):
        #Setter for the venue where the concert will be held
        #Venue must be of type Venue

        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        self._venue = venue
        
    def hometown_show(self):
    
        #Check if the concert is in the band's hometown
        #Returns:bool: True if the concert is in the band's hometown, False otherwise
        return self.venue.city == self.band.hometown

    def introduction(self):
        #Get the introduction for the concert
        #Returns:str: introduction for the concert

        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all = []  # list of all instances of Venue
    def __init__(self, name, city):
        #Initialize a Venue instance with a name and city
        self.name = name
        self.city = city
        Venue.all.append(self)  # add self to all instances

    @property
    def name(self):
        #Getter for the name of the venue
        
        return self._name
    
    @name.setter
    def name(self, name):
        #Setter for the name of the venue
        #name must be a non-empty string

        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be non-empty string")
        
    @property
    def city(self):
        #Getter for the city of the venue
        
        return self._city
    
    @city.setter
    def city(self, city):
        #Setter for the city of the venue
        #city must be a non-empty string

        if isinstance(city, str) and len(city):
            self._city = city
        else:
            raise ValueError("City must be non_empty string")

    def concerts(self):
        # get all concerts at this venue

        result =[concert for concert in Concert.all if concert.venue == self]
        return result if result else None

    def bands(self):
        # get unique bands that have played at this venue

        result = list(set(concert.band for concert in self.concerts()))
        return result if result else None
    
    def concert_on(self, date):
        # Returns the concert of a given date and None if the concert is not found.
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None

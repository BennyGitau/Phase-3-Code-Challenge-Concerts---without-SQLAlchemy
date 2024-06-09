class Band:
    all =[]
    def __init__(self, name, hometown):
        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("Hometown must be a non-empty string")
        self.name = name
        Band.all.append(self)
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("Name must be non-empty string")
    
    @property
    def hometown(self):
        return self._hometown 

    def concerts(self):
        concerts = [concert for concert in Concert.all if concert.band == self]
        return concerts if concerts else None

    def venues(self):
        venues = list(set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        return Concert(date, self, venue)


    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]



class Concert:
    all = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date):
            self._date = date
        else:
            raise ValueError("Date must be non-empty string")
        
    @property
    def band(self):
        return self._band
    @band.setter
    def band(self, band):
        if not isinstance(band, Band):
            raise TypeError("Band must be of type Band")
        self._band = band

    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, venue):
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        self._venue = venue
        

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all = []
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be non-empty string")
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city):
            self._city = city
        else:
            raise ValueError("City must be non_empty string")


    def concerts(self):
        result =[concert for concert in Concert.all if concert.venue == self]
        return result if result else None

    def bands(self):
        result = list(set(concert.band for concert in self.concerts()))
        return result if result else None
    
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None

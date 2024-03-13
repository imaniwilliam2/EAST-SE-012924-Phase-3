import ipdb

class Car: 

    def __init__(self, make, model, year, horn_volume = 1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

    def honk_horn(self):
        print(f"BEEP BEEP{'!' * self.horn_volume}")

    @property
    def year(self):
        return self._year
    

    @year.setter
    def year(self, year):
        if isinstance (year, int) and 1900 <= year <= 2023:
            self._year = year
        else:
            raise ValueError("Year must be an integer and must be between 1900 and 2023!")
        
    
    @property
    def horn_volume(self):
        return self._horn_volume
    
    @horn_volume.setter
    def horn_volume(self, horn_volume):
        if not isinstance(horn_volume, int):
            raise ValueError("Horn volume must be an integer!")
        self._horn_volume = horn_volume
        
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        if isinstance (make, str) and len(make) >= 3:
            self._make = make


car1 = Car("BMW", "I8", 2020, 8)
ipdb.set_trace()
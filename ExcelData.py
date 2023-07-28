class ExcelData:
    def __init__(self, date, booked, price,hotelOffice):
        self._date = date
        self._booked = booked
        self._price = price
        self._hotelOffice=hotelOffice

    # Getter and setter for name (string type)
    @property
    def date(self):
        print("Getting date...")
        return self._date

    @date.setter
    def date(self, value):
        print("Setting date...")
        self._date = value


    
    @property
    def booked(self):
        return self._booked

    @booked.setter
    def booked(self, value):
        self._booked = value

    # Getter and setter for age (integer type)
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer.")
        self._price = value

    # Getter and setter for salary (float type)
    @property
    def hotelOffice(self):
        return self._hotelOffice

    @hotelOffice.setter
    def hotelOffice(self, value):
        self._hotelOffice = value

#row = ExcelData("2023-07-26","YES",30,"Hotel To Office")

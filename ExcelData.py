class ExcelData:
    def __init__(self, date, hotelOffice, amount, exchRate, amountFC, remarks, booked):
        self._date = date
        self._hotelOffice=hotelOffice
        self._amount = amount
        self._exchRate=exchRate
        self._amountFC=amountFC
        self._remarks=remarks
        self._booked = booked
        
        



    # Getter and setter for name (string type)
    @property
    def date(self):
        print("Getting date...")
        return self._date

    @date.setter
    def date(self, value):
        print("Setting date...")
        self._date = value

    
    # Getter and setter for hotelOffice (string type)
    @property
    def hotelOffice(self):
        return self._hotelOffice

    @hotelOffice.setter
    def hotelOffice(self, value):
        self._hotelOffice = value


    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer.")
        self._amount = value

    # Getter and setter for exchRate (string type)
    @property
    def exchRate(self):
        return self._exchRate

    @exchRate.setter
    def exchRate(self, value):
        self._exchRate = value


    @property
    def amountFC(self):
        return self._amountFC

    @amountFC.setter
    def amountFC(self, value):
        self._amountFC = value

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value

    
    @property
    def booked(self):
        return self._booked

    @booked.setter
    def booked(self, value):
        self._booked = value


    

#row = ExcelData("2023-07-26","YES",30,"Hotel To Office")
#Update

#row = ExcelData('Date','Paticulars(From-To)' , 'Amount', 'Exch. Rate', 'Amount(FC)','Remarks(with bill/without bill)', 'Booked')
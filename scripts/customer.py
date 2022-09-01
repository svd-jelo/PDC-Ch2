#customer.py

from datetime import datetime
class Customer:
    """
    A class containing information about the customer that he/she provided in the registration. 
    This includes their name, address, and date of birth. Each instance is to be passed as the customer
    attribute of the corresponding `BankAccount` object.
    """

    def __init__(self, name, address, date_of_birth):
        """
        A method for initializing a Customer object. Contains the password of the bank account
        """

        self.name = name
        self.address = address
        self.date_of_birth = datetime.strptime(date_of_birth, '%B %d, %Y')
        self.password = '1234'

    def get_age(self):
        """
        A method for obtaining the customer's age today given the date of birth he/she entered 
        """

        today = datetime.today()
        try:
            birthday = self.date_of_birth.replace(year=today.year)
        except ValueError:
            # this will occur if the customer's birthday is Feb 29 but
            # today's year is not a leap year
            birthday = self.date_of_birth.replace(year = today.year, day = self.date_of_birth.day - 1)
        
        if birthday > today:
            return today.year - self.date_of_birth.year - 1
        return today.year - self.date_of_birth.year
from abc import ABC, abstractmethod

from RentalService import Rental

class Vehicle(ABC):
    def __init__(self, make, model, price):
        self._make = make
        self._model = model
        self._price = price
    
    @abstractmethod
    def calculate_premium(self):
        pass
    
    def __str__(self):
        return f"Vehicle [Make: {self._make}, Model: {self._model}, Price: {self._price}]"
    
class Car(Vehicle):
    def __init__(self, make, model, price,segment):
        super().__init__(make, model, price)
        self._segment = segment
        
    def calculate_premium(self):
        if self._segment == "Luxury":
            return 0.025 * self._price
        else :
            return self._price * 0.015
    
    def __str__(self):
        return super().__str__() + f"Segment : {self._segment}"
    
class Bike(Vehicle):
    
    def __init__(self, make, model, price,segment):
        super().__init__(make, model, price)
        self._segment = segment
        
    def calculate_premium(self):
        return self._price * 0.02
    
    def __str__(self):
        return super().__str__() + f"Segment : {self._segment}"
    

# b1 = Bike("Honda","NX200",280000,"Standard")
# print(b1)
# print(b1.calculate_premium())

# c1 = Car("MG","GLOSTER",1500000,"Luxury")
# print(c1)
# print(c1.calculate_premium())

# c2 = Car("MG","HECTOR",1500000,"Semi-Luxury")
# print(c2)
# print(c2.calculate_premium()) 

'''This code is written on day 5'''

class Taxi(Car,Rental):
    def __init__(self, make, model, price, segment,rental_id):
        Car.__init__(self ,make, model, price, segment)
        Rental.__init__(self,rental_id)
        
    def calculate_rent(self, hrs):
        if hrs <= 8:
            return hrs * 10000
        else:
            return hrs * 10000 + (hrs-8) * 500
    
    def calculate_premium(self):
        return super().calculate_premium()
    

taxi = Taxi('BMW','X6',150000,'Luxury',45)
print(taxi)
print(taxi.calculate_rent(7))
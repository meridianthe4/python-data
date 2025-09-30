'''This code is written on day 5'''

from VehiclePortal import Taxi,Bike
from RentalService import Rental

class RentalApp:
    @staticmethod
    def display_rent(rental_vechile : Rental):
            print("---Welcome to My Rental App----")
            hrs = int(input("Enter the hrs ")) 
            amt = rental_vechile.calculate_rent(hrs)
            print(f"total rent for {rental_vechile} is rs {amt}")
    
    
print("________USER________________")
taxi = Taxi('BMW','X6',150000,'Luxury',45)
RentalApp.display_rent(taxi)
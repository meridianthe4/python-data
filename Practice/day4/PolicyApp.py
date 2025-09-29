from VehiclePortal import Car,Bike,Vehicle

class Policy:
    @staticmethod
    def display_policy(vehicle : Vehicle):
        years = int(input("Enter how old is vehicle -> "))
        if years < 5:
            amount = vehicle.calculate_premium()
        else:
            amount = vehicle.calculate_premium() + 1000
        
        print(f"Total premiu, due for vehicle : {amount}")
        

'''Following coed is part of user module '''

my_car = Car('Honda','City',1500000,'ANY')
my_bike = Bike('Bajaj','XYZ',100000,'ANY')

Policy.display_policy(my_car)
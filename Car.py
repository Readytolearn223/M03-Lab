"""
 Michael Barnes 

 Veichles.ipynb

 The purpose of this program is to  take input of the info of your car and then output put the detail 
 of you car in a readable easy format. The variable veichle_type ,represnets the diffrent types of 
 veichle which could be a plan,truck or car, for this assigments  is cars . The year variable represent the year 
 of the car,the make represent the brand of the car , the model rerpesent the model of the car ,the doors variable 
 represents the number of doors of you car,and finally the roof simply represnet the type roof you have on your car
which is soild or a sun roof. 

"""


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def car_info():
    vehicle_type = "car"
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Do you have 2 doors or four doors on your car: ")
    roof = input("Is the roof of your car solid or a sun roof: ")
    return vehicle_type, year, make, model, doors, roof

def print_car_info(car):
    print("Vehicle type:", car.vehicle_type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Type of roof:", car.roof)

def main():
    vehicle_type, year, make, model, doors, roof = car_info()
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print("Car Details:")
    print_car_info(car)

if __name__ == "__main__":
    main()

  
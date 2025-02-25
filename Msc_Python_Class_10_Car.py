class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 500000
    def get_descriptive_name(self):
        long_name =f'{self.make} {self.model} {self.year}'
        return long_name.title()
    def read_odometer(self):
        print(f'The odometer is at {self.odometer_reading} miles')
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def incremenet_odometer(self,miles):
        self.odometer_reading += miles

    

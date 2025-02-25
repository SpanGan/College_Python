from Msc_Python_Class_10_Battery import Battery 
from Msc_Python_Class_10_Car import Car

class Electric_car(Car):
    def __init__(self, make, model, battery,year):
        super().__init__(make, model, year)
        self.battery = Battery(battery)
    def describe_battery(self):
        if 'chapri' in self.make.lower():
            self.size = 3
        
        print(f'Battery size is {self.battery.size}, and name is {self.battery.name}')
            

    def get_descriptive_name(self):
        long_name = super().get_descriptive_name()
        long_name += f' {self.battery.name}'
        return long_name.title()
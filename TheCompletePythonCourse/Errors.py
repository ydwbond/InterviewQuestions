class CustomError(TypeError):
    def __init__(self,msg, error_code):
        super().__init__(f'{msg}, Error Code {error_code}')
        self.code = error_code


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'< from {self.__class__}, make {self.make}, Model {self.model}>'


class Garage:
    """
    this class is Garage, to hold cars
    """
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    def __repr__(self):
        return f'<Garage with cars {self.cars}>'

    def add_cars(self, car):
        """
        :param car: Car Type
        :return: noe
        :add new car to Garage
        """
        if not isinstance(car,Car):
            raise CustomError("please use Car class",123)
        else:
            self.cars.append(car)


car1 = Car("Ford", "Focus")
car2 = Car("Honda", "Civic")


print(Garage.__doc__)
print(Garage.add_cars.__doc__)

g1 = Garage()
try:
    g1.add_cars(car1)
except :
    print("here")
else:
    print("else")
finally:
    print("finally")


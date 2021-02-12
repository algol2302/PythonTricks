class Car:
    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"{self.color.capitalize()} car with {self.mileage} mileage"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color!r}, {self.mileage!r})"


if __name__ == '__main__':
    car1 = Car(color="red", mileage=123123)
    car2 = Car(color="black", mileage=123)
    print(car1)
    print(car2)
    print([car1, car2])


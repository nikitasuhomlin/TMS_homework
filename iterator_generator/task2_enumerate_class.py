import enum

class Car(enum.Enum):
    ElectroCar = 1
    DieselCar = 2
    PetrolCar = 3

for car in Car:
    print(car)


#________________________

list(enumerate(['N', 'I', 'C', 'K']))
for a, b in enumerate(['N', 'I', 'C', 'K']):
    print(a, b)

    

# Создание своего класса 

class Cat():
    """ Модель кота"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Кот создан!')
    

    def jump(self):
        """ По команде кот прыгает"""
        print(self.name + ' запрыгнул на диван!')
       
    def hunger(self):
        """ Кот просит еду"""
        print(self.name + ' просит еду!')

    def thirst(self):
        """ Кот хочет пить"""
        print(self.name + ' просит налить ему воды!')

    def play(self):
        """ Кот хочет поиграть """
        print(self.name + ' хочет поиграть!')

    def toy(self):
        """ Кот просит, чтобы ему дали 
        игрушку"""
        print(self.name + ' просит игрушку!')

    def rat(self):
        """ Кот гоняется за 
        крысой"""
        print(self.name + ' гоняется за крысой!')
    
    def outdoors(self):
        """ Кот просится на 
        улицу"""
        print(self.name + ' просится на улицу!')

    def milk(self):
        """ Кот просит молока """
        print(self.name + ' просит молока!')



eva = Cat('Кошка Ева', 5)
bob = Cat('Кот Боб', 4)
maria = Cat('Кошка Мария', 6)
emily = Cat('Кошка Эмили',3)
martin = Cat('Кот Мартин', 6)
baton = Cat('Кот Батон',6)


eva.hunger()
maria.jump()
bob.thirst()
emily.play()
martin.rat()
baton.outdoors()

#____________________________________________

# Класс наследник

class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age) 

matroskin = Kitten('Котенок Матроскин', 0.4)
lolik = Kitten('Котенок Лолик', 0.3)
barmaley = Kitten('Котенок Бармалей', 0.3)
kuzya = Kitten('Котенок Кузя', 0.7)
mia = Kitten('Котенок Мия',0.6)
bulka = Kitten('Котенок Булка', 0.3)



matroskin.jump()
lolik.hunger()
barmaley.thirst()
kuzya.toy()
mia.play()
bulka.milk()

#_______________________________________________________

class Car():
    """ Создадим класс по созданию авто """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_name(self):
        print(self.make + ' ' + 
        self.model+ ' ' + str(self.year))


bmw = Car('BMW', 'M5',{2021})
audi = Car('Audi', 'RS8', {2021})
mercedes = Car('Mercedes', 'W222', {2021})


bmw.car_name()
audi.car_name()
mercedes.car_name()

class Hybrid(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)

toyota = Hybrid('Toyota', 'Camry Hybrid'
                , {2022})
hyundai = Hybrid('Hyundai',
                "Sonata Hybrid", {2022})
honda = Hybrid('Honda', 'Accord Hybrid',
                {2022})

toyota.car_name()
hyundai.car_name()
honda.car_name()

class Electric(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
tesla = Electric('Tesla','Plaid',{2022})
bmw_iX = Electric('BMW', 'iX',{2022})
porshe = Electric('Porsche', 'Taycan',{2022})

tesla.car_name()
bmw_iX.car_name()
porshe.car_name()






        
class Fruits:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        print(f"Фрукт: {self.name}, Цвет: {self.color}, Вес: {self.weight} г")


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel = 0

    def drive(self, city):
        print(f"Машина - {self.model} едет в - {city}")

    def refuel(self, amount):
        if amount <= 40:
            self.fuel += amount
            print(f"Бак пополнен на {amount} литров. Текущий уровень топлива: {self.fuel} л")
        else:
            print("Нельзя заправить больше 40 литров за раз")

    def drive_distance(self, city, distance):
        fuel_needed = distance / 10  # Расход топлива: 1 литр на 10 км
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            print(f"Машина - {self.model} едет в - {city}. Остаток топлива: {self.fuel} л")
        else:
            max_distance = self.fuel * 10  # Максимальное расстояние, которое может проехать машина
            print(f"Недостаточно топлива, чтобы доехать до {city}. Максимальное расстояние: {max_distance} км")


# Задание 1
fruit1 = Fruits("Яблоко", "Красное", 150)
fruit2 = Fruits("Груша", "Желтая", 200)
fruit3 = Fruits("Апельсин", "Оранжевый", 180)

fruit1.info()
fruit2.info()
fruit3.info()

# Задание 2
car1 = Car("Toyota Camry", 2022, "Серый")
car1.drive("Москва")
car1.refuel(30)
car1.drive_distance("Санкт-Петербург", 500)

# Доп. Задание
car2 = Car("BMW X5", 2023, "Черный")
car2.refuel(50)
car2.drive_distance("Новосибирск", 1500)

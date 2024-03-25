class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Привет, меня зовут {self.fullname}. Мне {self.age} лет. "
              f"{'Я женат/замужем.' if self.is_married else 'Я не женат/замужем.'}")


class Teacher(Person):
    salary = 0

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        self.salary = 20000 + self.experience * 3000

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Я преподаватель с {self.experience} годами опыта. Моя зарплата составляет {self.salary} рублей.")


# Создаем объект учителя
teacher1 = Teacher("Иван Иванов", 35, True, 10)

# Представляем учителя и считаем его зарплату
teacher1.calculate_salary()
teacher1.introduce_myself()

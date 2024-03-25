class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    def __make_computations(self, operator):
        if operator == '+':
            result = self.__cpu + self.__memory
        elif operator == '-':
            result = self.__cpu - self.__memory
        elif operator == '*':
            result = self.__cpu * self.__memory
        elif operator == '/':
            result = self.__cpu / self.__memory
        else:
            result = None
        return result
    
    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory
    
    def info(self):
        print(f"CPU: {self.get_cpu()}, Memory: {self.get_memory()}")


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
    
    def get_memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f"CPU: {self.get_cpu()}, Memory: {self.get_memory()}, Memory Card: {self.get_memory_card()}")


# Тестирование
computer = Computer(4, 8)
laptop = Laptop(3, 6, '64GB')

computer.info()
laptop.info()

print("Result of computation on Computer:", computer._Computer__make_computations('+'))
print("Result of computation on Laptop:", laptop._Computer__make_computations('*'))

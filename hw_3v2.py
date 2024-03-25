class Computer:
    def __init__(self, cpu, memory):
        self._cpu = cpu
        self._memory = memory
    
    @property
    def cpu(self):
        return self._cpu
    
    @property
    def memory(self):
        return self._memory
    
    def make_computations(self, operator):
        if operator == '+':
            result = self.cpu + self.memory
        elif operator == '-':
            result = self.cpu - self.memory
        elif operator == '*':
            result = self.cpu * self.memory
        elif operator == '/':
            result = self.cpu / self.memory
        else:
            result = None
        return result
    
    def info(self):
        print(f"CPU: {self.cpu}, Memory: {self.memory}")


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self._memory_card = memory_card
    
    @property
    def memory_card(self):
        return self._memory_card
    
    def info(self):
        print(f"CPU: {self.cpu}, Memory: {self.memory}, Memory Card: {self.memory_card}")


# Тестирование
computer = Computer(8, 16)
laptop = Laptop(6, 12, '256GB')

computer.info()
laptop.info()

print("Result of computation on Computer:", computer.make_computations('+'))
print("Result of computation on Laptop:", laptop.make_computations('*'))

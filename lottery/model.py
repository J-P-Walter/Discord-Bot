import random

class LotteryDrawing:
    numbers = []

    def __init__(self):
        self.numbers = self.draw_numbers()

    def draw_numbers(self):
        numbers = random.sample(range(1,59), k=6)
        return sorted(numbers)
        
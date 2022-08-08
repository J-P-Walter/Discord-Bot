import random
from mongoengine import *

class LotteryDrawing(Document):
    numbers = ListField()

    def draw_numbers(self):
        numbers = random.sample(range(1,59), k=6)
        return sorted(numbers)
        
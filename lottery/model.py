import random
from mongoengine import *
import datetime

class LotteryDrawing(Document):
    numbers = ListField()
    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.now)

    members_id = IntField(required=False)

    TYPE_USER = "user"
    TYPE_SYSTEM = "system"
    TYPE_CHOICES = [TYPE_USER, TYPE_SYSTEM]
    dtype = StringField(choices=TYPE_CHOICES, defualt=TYPE_USER)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now
        self.updated_at = datetime.datetime.now
        
        return super(LotteryDrawing, self).save(*args, **kwargs)

    def draw_numbers(self):
        numbers = random.sample(range(1,59), k=6)
        return sorted(numbers)
        
    def numbers_as_string(self):
        return ",".join(str(x) for x in self.numbers)
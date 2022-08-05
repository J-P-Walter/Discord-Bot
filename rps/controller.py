from .model import RPS
import random

class RPSGame():
    def run(self, user_choice):
        rps_instance = RPS()
        bot_choice = random.choice(rps_instance.get_choices())

       
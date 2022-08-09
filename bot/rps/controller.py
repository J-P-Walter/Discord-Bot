from .model import RPS
import random

class RPSGame():
    def run(self, user_choice):
        rps_instance = RPS()
        if user_choice not in rps_instance.get_choices():
            raise Exception("Invalid input: RPS")
        bot_choice = random.choice(rps_instance.get_choices())

        won = rps_instance.check_win(user_choice, bot_choice)
        return won, bot_choice
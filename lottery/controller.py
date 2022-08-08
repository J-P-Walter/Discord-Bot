from .model import LotteryDrawing


class LotteryController:
    def draw_numbers(self):
        drawing = LotteryDrawing()
        numbers = drawing.draw_numbers()
        return numbers

    def save(self, numbers):
        numbers = [int(x) for x in numbers.split(", ")]
        drawing = LotteryDrawing()
        drawing.numbers = numbers
        print("Saved")
        drawing.save()

from .model import LotteryDrawing


class LotteryController:
    def draw_numbers(self):
        drawing = LotteryDrawing()
        return drawing.numbers
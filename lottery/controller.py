from .model import LotteryDrawing


class LotteryController:
    def draw_numbers(self):
        drawing = LotteryDrawing()
        numbers = drawing.draw_numbers()
        return numbers

    def save(self, numbers, author=None):
        drawing = LotteryDrawing()
        drawing.numbers = numbers

        if author is not None:
            drawing.dtype = LotteryDrawing.TYPE_USER
            drawing.members_id = author.id
        else:
            drawing.dtype = LotteryDrawing.TYPE_SYSTEM
        drawing.save()

    def get_last_drawing(self):
        last_drawing = LotteryDrawing.objects.filter(dtype=LotteryDrawing.TYPE_SYSTEM).order_by("-created_at").first()
        return last_drawing

    def get_my_drawings(self, author):
        print("b")
        drawings = LotteryDrawing.objects.filter(members_id=author.id)
        print('c')
        return drawings
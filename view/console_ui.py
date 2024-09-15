from presenter.presenter import Presenter
from view.view import View


class ConsoleUI(View):

    def __init__(self):
        self.work = True
        self.presenter = Presenter(self)

    def print_answer(self, text: str):
        pass

    def start(self):
        pass

    def stop(self):
        self.work = False

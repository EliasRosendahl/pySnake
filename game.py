from model import Model
from view import View
from controller import Controller

def run():
    controller = Controller(View(), Model())
    controller.run()

if __name__ == "__main__":
    run()

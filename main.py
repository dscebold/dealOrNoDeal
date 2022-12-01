from deal import Deal
from dealController import *


def main():
    app = QApplication([])
    window = DealScreen()
    window.show()
    app.exec_()
    window.show()


if __name__ == '__main__':
    main()

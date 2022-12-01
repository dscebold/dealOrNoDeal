from PyQt5.QtWidgets import *
from Labs.src.dealOrNoDeal.deal_or_no_deal import *
from Labs.src.dealOrNoDeal.decision import *
import random as rand

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class DealScreen(QMainWindow, Ui_DealOrNoDeal):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.has_case = False
        self.current_case = None
        self.switch_cases = False
        self.open_case = False
        self.case_to_open = None
        # self.game = Deal()
        # self.game.run_game()
        self.cases = [self.case1, self.case2, self.case3, self.case4, self.case5, self.case6, self.case7, self.case8,
                      self.case9, self.case10, self.case11, self.case12, self.case13, self.case14, self.case15,
                      self.case16
            , self.case17, self.case18, self.case19, self.case20, self.case21,
                      self.case22, self.case23, self.case24, self.case25]
        self.case1.clicked.connect(lambda : self.case_choice(self.case1))
        self.case2.clicked.connect(lambda : self.case_choice(self.case2))
        self.case3.clicked.connect(lambda : self.case_choice(self.case3))
        self.case4.clicked.connect(lambda : self.case_choice(self.case4))
        self.case5.clicked.connect(lambda : self.case_choice(self.case5))
        self.case6.clicked.connect(lambda : self.case_choice(self.case6))
        self.case7.clicked.connect(lambda : self.case_choice(self.case7))
        self.case8.clicked.connect(lambda : self.case_choice(self.case8))
        self.case9.clicked.connect(lambda : self.case_choice(self.case9))
        self.case10.clicked.connect(lambda : self.case_choice(self.case10))
        self.case11.clicked.connect(lambda : self.case_choice(self.case11))
        self.case12.clicked.connect(lambda : self.case_choice(self.case12))
        self.case13.clicked.connect(lambda : self.case_choice(self.case13))
        self.case14.clicked.connect(lambda : self.case_choice(self.case14))
        self.case15.clicked.connect(lambda : self.case_choice(self.case15))
        self.case16.clicked.connect(lambda : self.case_choice(self.case16))
        self.case17.clicked.connect(lambda : self.case_choice(self.case17))
        self.case18.clicked.connect(lambda : self.case_choice(self.case18))
        self.case19.clicked.connect(lambda : self.case_choice(self.case19))
        self.case20.clicked.connect(lambda : self.case_choice(self.case20))
        self.case21.clicked.connect(lambda : self.case_choice(self.case21))
        self.case22.clicked.connect(lambda : self.case_choice(self.case22))
        self.case23.clicked.connect(lambda : self.case_choice(self.case23))
        self.case24.clicked.connect(lambda : self.case_choice(self.case24))
        self.case25.clicked.connect(lambda : self.case_choice(self.case25))
        self.decision = Decision()
        self.hold_case = None
        self.count = 0;
        self.decision.open_case.clicked.connect(lambda: self.open_click())
        self.decision.switch_case.clicked.connect(lambda: self.switch_click())
        rand.seed(400)
        self.holder = {}
        self.nums = []
        for i in range(1, 26):
            self.nums.append(i)
        values = [1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        for num in self.nums:
            temp = rand.choice(values)
            self.holder[num] = temp
            values.remove(temp)

    def case_choice(self, case):
        self.count += 1
        if not self.has_case:
            self.current_case = case
            for check_case in self.cases:
                if check_case == case:
                    check_case.hide()
            self.has_case = True
            self.money.setText(f"You currently have Case {self.current_case.text()}")
        else:
            self.hold_case = case
            self.decision.show()
            self.hide()


    def open_click(self):
        self.case_to_open = self.hold_case
        self.case_to_open.hide()
        self.show()
        self.decision.hide()
        if self.count == 25:
            self.money.setText(f"You currently have Case {self.current_case.text()} and won ${self.holder[int(self.current_case.text())]}")
        else:
            self.update_label()


    def switch_click(self):
        self.case_to_open = self.current_case
        self.current_case = self.hold_case
        for check_case in self.cases:
            if check_case == self.current_case:
                check_case.hide()
        self.show()
        self.decision.hide()
        if self.count == 25:
            self.money.setText(f"Your chose to switch to Case {self.current_case.text()} and won ${self.holder[int(self.current_case.text())]}")
        else:
            self.update_label()


    def update_label(self):
        self.money.setText(f"Your currently have Case {self.current_case.text()}\nYou opened Case {self.case_to_open.text()}"
                           f" and lost ${self.holder[int(self.case_to_open.text())]}")




class Decision(QMainWindow, Ui_decision):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.hide()






# class Deal:
#     def __init__(self):
#         self.cases = {}
#         self.set_cases()
#         print(4)
#
#     def set_cases(self):
#         rand.seed(400)
#         temp = 0
#         nums = []
#         for i in range(1, 26):
#             nums.append(i)
#         values = [1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
#         for num in nums:
#             temp = rand.choice(values)
#             self.cases[num] = temp
#             values.remove(temp)
#         print(self.cases)
#
#     def run_game(self):
#         current_case = 0
#         current_value = 0
#         choice = 0
#         opt = 0
#         temp = 0
#         print("Remaining Cases: ")
#         for key in self.cases:
#             print(key)
#         while True:
#             while True:
#                 try:
#                     choice = int(input("What case would you like to Start with?\n"))
#                     break
#                 except ValueError:
#                     print("THAT IS NOT A NUMBER!!!!!!")
#             if self.cases.get(choice) != -1:
#                 break
#             else:
#                 print("INVALID RESPONSE!!!")
#         current_case = choice
#         current_value = self.cases[current_case]
#         self.cases.pop(current_case)
#         while len(self.cases) > 1:
#             print("Remaining Cases: ")
#             for key in self.cases:
#                 print(key)
#             while True:
#                 while True:
#                     try:
#                         choice = int(input("What case would you like to interact with?\n"))
#                         break
#                     except ValueError:
#                         print("THAT IS NOT A NUMBER!!!!!!")
#                 if self.cases.get(choice, -1) != -1:
#                     break
#                 else:
#                     print("INVALID RESPONSE!!!")
#             while True:
#                 while True:
#                     try:
#                         opt = int(input("What would you like to do?\n1. Open Case\n2. Switch Cases?\n"))
#                         break
#                     except ValueError:
#                         print("THAT IS NOT A NUMBER!!!!!!")
#                 if opt == 1 or opt == 2:
#                     break
#                 else:
#                     print("INVALID RESPONSE!!!")
#             if opt == 1:
#                 print(f"Case {choice} contained ${self.cases.get(choice)}")
#                 self.cases.pop(choice)
#             elif opt == 2:
#                 temp = current_case
#                 current_case = choice
#                 choice = temp
#                 print(f"Case {choice} contained ${current_value}")
#                 current_value = self.cases[current_case]
#                 self.cases.pop(current_case)
#         while True:
#             while True:
#                 try:
#                     opt = int(input("What would you like to do?\n1. Open Case\n2. Switch Cases?\n"))
#                     break
#                 except ValueError:
#                     print("THAT IS NOT A NUMBER!!!!!!")
#             if opt == 1 or opt == 2:
#                 break
#             else:
#                 print("INVALID RESPONSE!!!")
#         if opt == 1:
#             print(f"You had Case {current_case} and won ${current_value}")
#         elif opt == 2:
#             for key in self.cases:
#                 choice = key
#             print(f"You chose to switch to Case {choice} and won ${self.cases.get(choice)}")


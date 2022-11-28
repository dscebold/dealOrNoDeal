import random as rand


class Deal:

    def __init__(self):
        self.cases = {}
        self.set_cases()
        print(4)

    def set_cases(self):
        rand.seed(400)
        temp = 0
        nums = []
        for i in range(1, 26):
            nums.append(i)
        values = [1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        for num in nums:
            temp = rand.choice(values)
            self.cases[num] = temp
            values.remove(temp)
        print(self.cases)

    def run_game(self):
        current_case = 0
        current_value = 0
        choice = 0
        opt = 0
        temp = 0
        print("Remaining Cases: ")
        for key in self.cases:
            print(key)
        while True:
            while True:
                try:
                    choice = int(input("What case would you like to Start with?\n"))
                    break
                except ValueError:
                    print("THAT IS NOT A NUMBER!!!!!!")
            if self.cases.get(choice) != -1:
                break
            else:
                print("INVALID RESPONSE!!!")
        current_case = choice
        current_value = self.cases[current_case]
        self.cases.pop(current_case)
        while len(self.cases) > 1:
            print("Remaining Cases: ")
            for key in self.cases:
                print(key)
            while True:
                while True:
                    try:
                        choice = int(input("What case would you like to interact with?\n"))
                        break
                    except ValueError:
                        print("THAT IS NOT A NUMBER!!!!!!")
                if self.cases.get(choice, -1) != -1:
                    break
                else:
                    print("INVALID RESPONSE!!!")
            while True:
                while True:
                    try:
                        opt = int(input("What would you like to do?\n1. Open Case\n2. Switch Cases?\n"))
                        break
                    except ValueError:
                        print("THAT IS NOT A NUMBER!!!!!!")
                if opt == 1 or opt == 2:
                    break
                else:
                    print("INVALID RESPONSE!!!")
            if opt == 1:
                print(f"Case {choice} contained ${self.cases.get(choice)}")
                self.cases.pop(choice)
            elif opt == 2:
                temp = current_case
                current_case = choice
                choice = temp
                print(f"Case {choice} contained ${current_value}")
                current_value = self.cases[current_case]
                self.cases.pop(current_case)
        while True:
            while True:
                try:
                    opt = int(input("What would you like to do?\n1. Open Case\n2. Switch Cases?\n"))
                    break
                except ValueError:
                    print("THAT IS NOT A NUMBER!!!!!!")
            if opt == 1 or opt == 2:
                break
            else:
                print("INVALID RESPONSE!!!")
        if opt == 1:
            print(f"You had Case {current_case} and won ${current_value}")
        elif opt == 2:
            for key in self.cases:
                choice = key
            print(f"You chose to switch to Case {choice} and won ${self.cases.get(choice)}")


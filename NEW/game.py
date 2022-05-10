import random
import time
import json

from user import User








class Game:

    def __init__(self, user : User, diff : int, type : int, turns : int):

        self.User = user
        self.diff = diff
        self.type = type
        self.turns = turns
        self.isover = False
        if self.User == None:
            self.free = True
        else:
            self.free = False
        self.duration = None
        self.points = 0



    def __call__(self):

        if not self.isover:
            print("You will see a series of operations one at a time.\nYou will have to type out the number you think is the result.\nYou can skip a question by pressing enter but it will have a negative impact on your final score.\nOn the other hand if your answer is wrong the impact will be bigger\nOnce you press enter the timer and the game will start")
            input("ready?")

            start_time = time.time()

            #addittion
            if self.type == 1:
                for i in range(self.turns):
                    
                    x = random.randint(-50, 50)*self.diff
                    y = random.randint(-50, 50)*self.diff
                    res = x + y
                    answer = input("result:")

                    if str(res) == answer:
                        print("correct")
                        self.points += 1

                    elif answer == "":
                        print("skipped")
                        self.points -= 1

                    else:
                        print("wrong")
                        self.points -= 2

            #subtraction
            elif self.type == 2:
                for i in range(self.turns):

                    x = random.randint(-50, 50)*self.diff
                    y = random.randint(-50, 50)*self.diff
                    res = x + y
                    answer = input("result:")

                    if str(res) == answer:
                        print("correct")
                        self.points += 1

                    elif answer == "":
                        print("skipped")
                        self.points -= 1

                    else:
                        print("wrong")
                        self.points -= 2


            #multiplication
            elif self.type == 3:
                for i in range(self.turns):

                    x = random.randint(-10, 10)*self.diff
                    y = random.randint(-10, 10)*self.diff
                    res = x + y
                    answer = input("result:")

                    if str(res) == answer:
                        print("correct")
                        self.points += 1

                    elif answer == "":
                        print("skipped")
                        self.points -= 1

                    else:
                        print("wrong")
                        self.points -= 2


            #division
            else:
                a = lambda n :  a(random.randint(-10, 10)) if n == 0 else n
                
                for i in range(self.turns):

                    x = random.randint(-10, 10)*self.diff
                    y = random.randint(-10, 10)*self.diff
                    y = a(y)

                    res = x / y
                    answer = input("result:")

                    if str(res) == answer:
                        print("correct")
                        self.points += 1

                    elif answer == "":
                        print("skipped")
                        self.points -= 1

                    else:
                        print("wrong")
                        self.points -= 2


            self.duration = time.time() - start_time
            self.isover = True

        else:
            raise("game object already been played")






    def calculate(self):

        if self.isover == True:
            score = int(self.diff*self.points/(self.duration/self.type/1000))

            if score > self.User.high_score:
                self.User._json["high score"] = score

                with open(self.User.file , mode = "w") as f:
                    f.write(json.dumps(self.User._json))

        else:
            return False



    @classmethod
    def setup_game(cls, user : User):
        
        print("Choose a game type\n1.addition\n2.#subtraction\n3.multiplication\n4.division")
        _type = input("choice:")

        while not isinstance(_type, int) or not (str(_type) in ["1", "2", "3", "4"]):

            try:
                _type = int(_type)
                if not (_type in [1, 2, 3, 4]):
                    _type = int(input("Input needs to be a number between 1 and 4"))

            except ValueError:
                _type = input("Input needs to be a number:")


        diff = input("Choose a difficulty (choice needs to be a positive integer):")
        while not ( isinstance(diff, int) or diff <= 0):
            print("invalid choice")
            diff = ("choice:")


        _turns = input("Choose how many turns you want (choice needs to be a positive integer):")
        while not ( isinstance(_turns, int) or _turns <= 0):
            print("invalid choice")
            _turns = ("choice:")
        

        return cls(user, diff, _type, _turns)
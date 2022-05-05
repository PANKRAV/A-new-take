import random
import time
import os
import json
import random



class User:
    user_count = 0

    def __init__(self, name : str):
        dirs = os.listdir()

        self.name = name
        self.file = f"{self.name}.json"
        self.high_score = None

        if self.file not in dirs:
            self._json = {"name" : self.name, "high score" : self.high_score}
            w_json = json.dumps(self._json, indent = 4)

            with open(self.file, mode = "w") as f:
                f.write(w_json)

        else:
            with open(self.file, mode = "r") as f:
                self._json = json.loads(f.read())
                self.high_score = self._json["hight score"]



        User.user_count += 1


    

    def __str__(self) -> str:
        if self.name[-1].upper() == "S":
            return f"{self.name}\' high score is:\n{self.high_score}"   
        else:
            return f"{self.name}\'s high score is:\n{self.high_score}"







class Game:

    def __init__(self, user : User, diff : int, type : int, turns : int):

        self.User = user
        self.diff = diff
        self.type = type
        self.turns = turns
        self.isover = False
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

    
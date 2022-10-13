import random
import time
import json
from numpy import isin

from user import User



class AlreadyPlayed(Exception):
    pass




class Game:

    def __init__(self, user : User, diff : int, _type : int, turns : int):

        self.User = user
        self.diff = diff
        self._type = _type
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
            if self._type == 1:
                for i in range(self.turns):
                    
                    x = random.randint(-50, 50)*self.diff
                    y = random.randint(-50, 50)*self.diff
                    res = x + y
                    if y < 0 :
                        answer = input(f"{x}{y}:")
                    else :
                        answer = input(f"{x}+{y}:")

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
            elif self._type == 2:
                for i in range(self.turns):

                    x = random.randint(-50, 50)*self.diff
                    y = random.randint(-50, 50)*self.diff
                    res = x - y
                    if y < 0 :
                        answer = input(f"{x}+{y}:")
                    else :
                        answer = input(f"{x}{y}:")

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
            elif self._type == 3:
                for i in range(self.turns):

                    x = random.randint(-10, 10)*self.diff
                    y = random.randint(-10, 10)*self.diff
                    res = x + y
                    if y < 0 :
                        answer = input(f"{x}x({y}):")
                    else :
                        answer = input(f"{x}x{y}:")

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
                    if y < 0 :
                        answer = input(f"{x}/({y}):")
                    else :
                        answer = input(f"{x}/{y}:")

                    if str(res) == answer:
                        print("correct")
                        self.points += 1

                    elif answer == "":
                        print("skipped")
                        self.points -= 1

                    else:
                        print("wrong")
                        self.points -= 2


            
            self.isover = True

            
            self.total_time = time.time() - start_time
            avg_time = (self.total_time)/self.turns
            score = self.calculate()
            print(f"Your score was {score}\nYou completed your game in {self.total_time} with an avergae time spent per question of {avg_time}")
            del score


        else:
            raise AlreadyPlayed("game object already been played")








    def calculate(self):

        if self.isover == True:
            score = int(self.diff*self.points/(self.total_time/self._type/1000))


            if self.User != None :
                if score > self.User.high_score:
                    self.User.data = ["high score", score]
                    self.User.high_score = score

                    with open(self.User.file , mode = "w") as f:
                        f.write(json.dumps(self.User._json))
            return score
        else:
            return False






    @classmethod
    def setup_game(cls, user : User):

        
        print("Choose a game type\n1.addition\n2.#subtraction\n3.multiplication\n4.division")
        _type = input("choice:")
        while True :
            try:
                _type = int(_type)
            except:
                _type = input("game type needs to be an integer:")
                continue
                            
            if _type <= 0 :
                _type = input("game type needs to be a positive integer:")
                continue

            if _type not in [1, 2, 3, 4] :
                _type = input("game type needs to be a postitive integer between 1 and 4:")
                continue

            break




        
        print("Choose a difficulty (choice needs to be a positive integer)")
        diff = input("choice:")
        while True :         
            try:
                diff = int(diff)
            except:
                diff = input("diff type needs to be an integer:")
                continue
            
            if diff <= 0 :
                diff = ("diff needs to be a positive integer:")
                continue

            break






        print("Choose a number of turns (choice needs to be a positive integer)")
        turns = input("choice:")
        while True :
            try:
                turns = int(turns)
            except:
                turns = input("turns number needs to be an integer:")
                continue

            if turns <= 0 :
                turns = ("turns number needs to be a positive integer:")
                continue

            break
        

        return cls(user, diff, _type, turns)




    @classmethod
    def load_json(cls, user : User, num : int) :
        game = user.customs[num]
        diff = game["diff"]
        _type = game["_type"]
        turns = game["turns"]
        return cls(user, diff, _type, turns)
        

    
    
    def json_pack(self) :
        self.User.customs.append({"diff" : self.diff, "_type" : self._type, "turns" : self.turns})
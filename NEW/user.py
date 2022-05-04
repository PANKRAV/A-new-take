import random
import time



class User:
    user_count = 0

    def __init__(self, name : str):

        self.name = name
        self.file = f"{self.name}.json"
        self.high_score = None

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



    def __call__(self):

        start_time = time.time()

        #addittion
        if self.type == 1:
            for i in range(self.turns):
                x = random.randint(1, 50)*self.diff
                y = random.randint(1, 50)*self.diff


        #subtraction
        elif self.type == 2:
            for i in range(self.turns):
                x = random.randint(1, 50)*self.diff
                y = random.randint(1, 50)*self.diff

        #multiplication
        elif self.type == 3:
            for i in range(self.turns):
                x = random.randint(1, 10)*self.diff
                y = random.randint(1, 10)*self.diff


        #division
        else:
            for i in range(self.turns):
                x = random.randint(1, 10)*self.diff
                y = random.randint(1, 10)*self.diff

        duration = time.time() - start_time


    def calculate(self):
        return 

    
import random
import time
import os
import json
import random

from _utility import dir_reset
if __name__ == "__main__": from game import Game

class ReadOnly(Exception):
    pass




class User:
    user_count = 0
    user_data = dict({})

    def __init__(self, name : str):
        dirs = os.listdir()

        self.name = name

        self.high_score = None

        if self.file not in dirs:
            self._json = {"name" : self.name, "high score" : self.high_score}
            w_json = json.dumps(self._json, indent = 4)

            with open(self.file, mode = "w") as f:
                f.write(w_json)

        else:
            with open(self.file, mode = "r") as f:
                self._json = json.loads(f.read())
                self.high_score = self._json["high score"]



        User.user_count += 1


    def __str__(self) -> str:
        if self.name[-1].upper() == "S":
            return f"{self.name}\' high score is:\n{self.high_score}"   
        else:
            return f"{self.name}\'s high score is:\n{self.high_score}"



    @property
    def file(self) :
        return f"{self.name}.json"


    @file.setter
    def file(self, value) :
        raise ReadOnly("file atributte cannot be setted")
        

    @staticmethod
    def create_users():

        dir_reset()
        os.chdir("data/userData")
        dirs = os.listdir()
        names = [name.rstrip(".json") for name in dirs]
        for name in names:
            User.user_data[name] = User(name)



     
import random
import time
import os
import json
import random

from _utility import dir_reset
if __name__ == "__main__": from game import Game

class ReadOnly(Exception):
    pass

class BadValue(Exception):
    pass




class User:
    user_count = 0
    user_data = dict({})

    def __init__(self, name : str):
        dirs = os.listdir()

        self.name = name

        self.high_score = 0
        self.customs = []

        if self.file not in dirs:
            w_json = json.dumps(self.data, indent = 4)

            with open(self.file, mode = "w") as f:
                f.write(w_json)
                
                



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




    @property
    def data(self) :
        return {"name" : self.name, "high score" : self.high_score, "customs" : self.customs}

    """
    @data.setter
    def data(self, args : list) :
        for el in args :
            if el[0] == "custom" :
                for custom in el[1] :
                    self.customs.append(custom)
            elif el[0] == "name" :
                self.name == el[1]
            elif el[0] == "high_score" :
                self.high_score == el[1]
            
            else:
                raise BadValue("provide a list with the first element being a string (custom, name or high_score) and second element being the actual data")
    """


    @property
    def _json(self) :
        dir_reset()
        os.chdir("data/userData")
        with open(self.file, "r") as f :
            self._json_ = f.read()
        os.chdir("../..")
        return self._json_
        



    @_json.setter
    def _json(self, value) :
        dir_reset()
        os.chdir("data/userData")
        with open(self.file, "w") as f :
            f.write(json.dumps(value, indent = 4))
        
        

    @staticmethod
    def create_users():

        dir_reset()
        os.chdir("data/userData")
        dirs = os.listdir()
        names = [name.rstrip(".json") for name in dirs]
        for name in names:
            User.user_data[name] = User(name)



    def save(self) :
        dir_reset()
        os.chdir("data/userData")
        
        
        with open(self.file, mode = "w") as f:
                f.write(json.dumps(self.data, indent = 4))


     
#default
import json
import time
import os
import tkinter as tk
import sys
import matplotlib.pyplot as plt
import numpy as np
import pyautogui as pg

#user defined
from user import User
from game import Game
from _utility import dir_reset


#constants
gameLoop = True







def init():
    dir_reset()

    dirs = os.listdir()

    if "setup" not in dirs:
        os.system("python setup.py")

    User.create_users()








def main():
    init()




    while gameLoop:
        choice = input("1.New Player\n2.Select Player\n3.Free Play\n4.Exit\nchoice:")


        while True :
            try:
                choice = int(choice)
            except :
                choice = input("choice needs to be an integer:")
                continue

            if choice <= 0 :
                choice = input("choice needs to be a poistive integer:")
                continue

            if choice not in [1, 2, 3, 4] :
                choice = input("choice needs to be a integer between 1 and 4:")
                continue
            break


        os.system("cls || clear")



        if choice == 1:
            try:
                os.chdir("../data/userData")

            except:
                print(os.listdir()) #debugging

            dirs = os.listdir()

            while True:

                name = input("input a name:")

                if name not in User.user_data.keys():
                    User.user_data[name] = User(name)
                    break

                else:
                    print("user already exists")


            os.system("cls || clear")

        elif choice == 2:
            name = input("Give player name:")

            while name not in User.user_data.keys():
               print("Player does not exist")
               name = input("give another name:")


            current : User = User.user_data[name]

            while True :
                os.system("cls || clear")
                print("1.New Game\n2.Load Game\n3.Create Game\n4.See High Score\n5.Back")
                choice = input("choice:")

                while True :
                    try:
                        choice= int(choice)

                    except:
                        choice = input("choice needs to be an integer:")
                        continue

                    if choice <= 0 :
                        choice = input("choice needs to be a poistive integer:")
                        continue

                    if choice not in [1, 2, 3, 4, 5] :
                        choice = input("choice needs to be a integer between 1 and 5:")
                        continue
                    break


                if choice == 1 :
                    game = Game.setup_game(current)
                    game()

                elif choice == 2 :
                    custom = Game.setup_game(current)
                    custom.json_pack()
                
                elif choice == 3 :
                    ...

                else:
                    ...

            

        elif choice == 3 :
            free_game = Game.setup_game(None)
            free_game()


        else:
            sys.exit()





if __name__ == "__main__":
    main()
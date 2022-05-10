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
from user import User, Game
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


        while not isinstance(choice, int) or not (str(choice) in ["1", "2", "3", "4"]):

            try:
                choice = int(choice)
                if not (choice in [1, 2, 3, 4]):
                    choice = int(input("Input needs to be a number between 1 and 4"))

            except ValueError:
                choice = input("Input needs to be a number:")


        os.system("cls || clear")



        if choice == 1:
            os.chdir("data/userData")

            dirs = os.listdir()

            while True:

                name = input("input name:")

                if name not in User.user_data.keys():
                    User(name)
                    break

                else:
                    print("user already exists")


            os.system("cls || clear")

        elif choice == 2:
            name = input("Give player name:")

            while name not in User.user_data.keys():
               print("Player does not exist")
               name = input("give another name:")


            game = Game.setup_game(User.user_data[name])

            

        elif choice == 3 :
            free_game = Game.setup_game(None)


        else:
            sys.exit()





if __name__ == "__main__":
    main()
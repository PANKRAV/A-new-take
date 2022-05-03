#default
import json
from posixpath import dirname
import time
import os
import tkinter as tk
import sys
import matplotlib.pyplot as plt
import numpy as np
import pyautogui as pg

#user defined
import user

def init():
    abspath = os.path.abspath(__file__)
    dirName = os.path.dirname(abspath)
    os.chdir(dirName)
    
    dirs = os.listdir()

    if "setup" not in dirs:
        os.system("python setup.py")




def main():
    init()

    choice = input("1.New Player\n2.Select Player\n3.Just Play\n4.Exit\nchoice:")


    while not isinstance(choice, int) or not (str(choice) in ["1", "2", "3", "4"]):

        try:
            choice = int(choice)
            if not (choice in [1, 2, 3, 4]):
                choice = int(input("Input needs to be a number between 1 and 4"))

        except ValueError:
            choice = input("Input needs to be a number:")

    
    os.system("cls || clear")




if __name__ == "__main__":
    main()
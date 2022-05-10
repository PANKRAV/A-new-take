import os


def dir_reset():
    abspath = os.path.abspath(__file__)
    dirName = os.path.dirname(abspath)
    os.chdir(dirName)




def handle_file(ctx : str, opt : str = "read"):
    pass
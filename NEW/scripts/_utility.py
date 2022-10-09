import os


def dir_reset():
    abspath = os.path.abspath(__file__)
    dirName = os.path.dirname(abspath)
    dirname = os.path.join("../", dirName)
    os.chdir(dirName)

#test


def handle_file(ctx : str, opt : str = "read"):
    pass
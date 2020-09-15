import os


def working_dir(wDir):
    if not os.path.exists(wDir):
        os.mkdir(wDir)
    os.chdir(wDir)
    return os.path.abspath(wDir)

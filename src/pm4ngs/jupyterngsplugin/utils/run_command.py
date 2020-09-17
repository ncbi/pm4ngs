import os


def run_command(cmd):
    print('Executing: ' + cmd)
    r = os.system(cmd)
    print(r)

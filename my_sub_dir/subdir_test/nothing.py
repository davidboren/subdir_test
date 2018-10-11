import os


def do_stuff():
    print("USER: {}".format(os.getenv('USER')))


if __name__ == 'main':
    do_stuff()

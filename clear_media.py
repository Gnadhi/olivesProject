# WARNING
# THIS IS A SCRIPT DESIGNED To QUICKLY CLEAR ALL THE FILES IN THE MEDIA FOLDER
# THIS FILE SHOULD NOT BE RELEASED IN THE FINAL BUILD OF THE WEBSITE

import os
from os import walk
from olivesProject.settings import MEDIA_DIR


def clear():

    for dirpath, subdirs, files in walk(MEDIA_DIR):
        for file in files:
            print("Deleting file: " + os.path.join(dirpath, file))
            os.remove(os.path.join(dirpath, file))


if __name__ == "__main__":
    confirm = input("WARNING THIS WILL CLEAR ALL FILES IN THE MEDIA DIR. ENTER y TO CONTINUE: ")
    if confirm == "y":
        print("CONFIRMATION ACKNOWLEDGED DELETING ALL MEDIA FILES !")
        clear()

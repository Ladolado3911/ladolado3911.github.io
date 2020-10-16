from django.shortcuts import render

import pyautogui, sys
import pyscreeze
import os
import os, sys, stat
import shutil
from pathlib import Path

class Desktop(object):

    def __init__(self):
        self.switch = False
        self.username = username = os.getlogin()
        #print(os.path.join(os.environ["HOMEPATH"], "Desktop"))
        self.path = os.path.join(os.environ["HOMEPATH"], "Desktop")
        #self.test_and_create_files()
        self.lst = ["programs", "gifs", "pictures", "videos", "projects", "files", "songs", "shortcuts"]


    def switchh(self, switch1):
        try:
            int(switch1)
            print("Please type in yes or no")
        except:
            switch_lower = switch1.lower()
            if switch_lower not in ["yes", "no"]:
                print("Please type in yes or no")
            else:
                if switch_lower == "yes":
                    self.switch = True
                else:
                    self.switch = False



    def test_and_create_files(self):

        desk = list(os.listdir(rf"{self.path}"))
        lower_desk = []

        os.chdir(self.path)

        #print(desk)

        if self.switch == False:
            print("Desktop is off! Use Switch First")
        else:
            for a in desk:
                for b in self.lst:
                    if a.lower() == b:
                        os.chmod(f"{a}", stat.S_IWRITE)
                        os.rename(f"{a}", f"{a.lower()}")
                    else:
                        continue

            for b in self.lst:
                if b not in desk:
                    try:
                        os.mkdir(f"{b}")
                    except:
                        pass
                else:
                    continue


class Folder(object):

    def __init__(self, name):
        self.name = name
        extensions = []
        desktop_obj = Desktop()
        desktop_obj_path = desktop_obj.path

        self.path = rf"{desktop_obj_path}\\{name}"
        self.content = self.list_content()

    def list_content(self):
        content = list(os.listdir(self.path))

        return content


class Videos(Folder):
    pass


############################### code this class later
class Sub_Folder(Folder):
    pass
############################## code this class later



# Create your views here.

def index(request):
    return render(request, "desk/button.html")

def action(request):
    folder_obj = Folder("videos")
    print(folder_obj.content)

    desk_obj = Desktop()
    desk_obj.switchh("yes")
    desk_obj.test_and_create_files()

    print(os.path.join(os.environ["HOMEPATH"], "Desktop"))

    return render(request, "desk/button.html")






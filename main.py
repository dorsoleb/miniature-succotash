import os, fnmatch
import numpy as np
import cv2
from mss.linux import MSS as mss
import time
import pyautogui as pg
import imutils
import mss
import numpy
import pyautogui
from PIL import ImageGrab, Image
from cvimage_class import Cvimage
current_path = os.getcwd()

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

class CreepImage(object):

    def __init__(self, img_path, file_name, deep_search):
        self.img_path = img_path
        self.file_name = file_name
        self.deep_search = deep_search
        self.template_path = img_path + file_name

        self.cvimage = Cvimage(self.template_path)

def main():

    img_path = current_path + '\\img\\' + '\\kor_template\\'
    test_gameplay = current_path + '\\img\\' + '\\kor_template\\' + '\\test_like_vid\\'
    hui_list = find('*.png', test_gameplay)
    search_in_img_filename = 'test_img.jpg'
    search_in_img_path = img_path + search_in_img_filename 

    deep_search1 = {'top_flip': 0.71, 'top': 0.7, 'bot_flip': 0.6, 'bot': 0.6}
    creep1 = CreepImage(img_path, 'creep1.png', deep_search1)

    deep_search2 = {'top_flip': 0.80, 'top': 0.7, 'bot_flip': 0.80, 'bot': 0.75}
    creep2 = CreepImage(img_path, 'creep2.png', deep_search2)

    deep_search3 = {'top_flip': 0.71, 'top': 0.7, 'bot_flip': 0.7, 'bot': 0.6}
    creep3 = CreepImage(img_path, 'creep3.png', deep_search3)

    deep_search4 = {'top_flip': 0.71, 'top': 0.7, 'bot_flip': 0.7, 'bot': 0.6}
    creep4 = CreepImage(img_path, 'creep4.png', deep_search4)
#    template_base = Cvimage(template_path)
#    template_base2 = Cvimage(template_path2)
#    template_base3 = Cvimage(template_path3)
#
    for find_in_img_path in hui_list:
        find_in_img = Cvimage(find_in_img_path)
        find_in_img.find_by_template(creep1.cvimage, creep1.deep_search, debug=True)
        find_in_img.find_by_template(creep2.cvimage, creep2.deep_search, debug=True)
        find_in_img.find_by_template(creep3.cvimage, creep3.deep_search, debug=True)
        find_in_img.find_by_template(creep4.cvimage, creep4.deep_search, debug=True)

if __name__ == "__main__":

    main()

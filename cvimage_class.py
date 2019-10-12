
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

from utils import func_name
from PIL import ImageGrab, Image

current_path = os.getcwd()

class Cvimage(object):
#    img_path = None
#    img = None
#    file_name = None

    def __init__(self, img_path):
        self.img_path = img_path
        self.file_name =  self.img_path.split("\\")[-1]
        self.img = self.get_img()
        self.gray_img = self.get_gray_img()
        self.top_crop, self.bot_crop = self.half_crop_img(self.gray_img)

    def get_img(self, gray=False):
        return cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE) if gray else cv2.imread(self.img_path) 

    def get_gray_img(self):
            #cv2.imshow('Detected', img)
            #cv2.waitKey(0)
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    
    def get_flip(self, img):
        return cv2.flip(img, 1)

    def get_shape(self):
        h, w, *_ = self.img.shape
        return h, w 
    
    def show_img(self, img, description='Show Img func'):
        cv2.imshow(description, img) 
        print("Press any key to continue")
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

    def half_crop_img(self, img):
        height, width = self.get_shape()

        # Crop top 
        start_row, start_col = int(0), int(0)
        end_row, end_col = int(height * .5), int(width)
        cropped_top = img[start_row:end_row , start_col:end_col]
        
        # Crop bottom 
        start_row, start_col = int(height * .5), int(0)
        end_row, end_col = int(height), int(width)
        cropped_bot = img[start_row:end_row , start_col:end_col]

        #self.show_img(cropped_top)
        #self.show_img(cropped_bot)
        return cropped_top, cropped_bot


    def find_by_template(self, template, debug=False):
        #template.make_flip()
        #cv2.imshow('Detected', template.img)
        #cv2.imshow('Detected', template.img)
        #cv2.waitKey()
        #import ipdb; ipdb.set_trace()
        res = cv2.matchTemplate(self.gray_img, template.gray_img, cv2.TM_CCOEFF_NORMED) 
        def draw_find(res, self, template, threshold=0.51):
            #threshold = 0.51
            loc = np.where( res >= threshold) 
            if len(loc[0]):
                w, h = template.get_shape() 
                for pt in zip(*loc[::-1]): 
                    cv2.rectangle(self.img, pt, (pt[0] + w, pt[1] + h), (168, 64, 165), 2)
                    
                cv2.imshow('Detected', self.img)
                cv2.waitKey(0)
            else:
                file_name = template.img_path.split("\\")
                #print('cant detect => ', file_name[-1])
            return bool(len(loc[0]))

        if debug:
            finded = draw_find(res, self, template)
            if finded:
                print('i found by img')
        loc = np.where( res >= 0.6) 
        #import ipdb; ipdb.set_trace()
        if not loc[0]:
            #print('hmm i cant find loc, using crop')
            res_crop_top = cv2.matchTemplate(self.gray_img, template.top_crop, cv2.TM_CCOEFF_NORMED)
            res_crop_top_flip = cv2.matchTemplate(self.gray_img, self.get_flip(template.top_crop), cv2.TM_CCOEFF_NORMED)
            res_crop_bot = cv2.matchTemplate(self.gray_img, template.bot_crop, cv2.TM_CCOEFF_NORMED)
            res_crop_bot_flip = cv2.matchTemplate(self.gray_img, self.get_flip(template.bot_crop), cv2.TM_CCOEFF_NORMED)
            
            my_threshold = 0.6
            top = draw_find(res_crop_top, self, template, 0.6)
            top_flip = draw_find(res_crop_top_flip, self, template, my_threshold)

            bot = draw_find(res_crop_bot, self, template, 0.6)
            if top:
                print('i found by top_crop')

            if bot:
                print('i found by bot_crop')
        return res






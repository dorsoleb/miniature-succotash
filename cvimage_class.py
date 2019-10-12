
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
        self.top, self.bot = self.half_crop_img(self.gray_img)
        self.top_flip = self.get_flip(self.top)
        self.bot_flip = self.get_flip(self.bot)

    def get_img(self, gray=False):
        return cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE) if gray else cv2.imread(self.img_path) 

    def get_gray_img(self):
            #cv2.imshow('Detected', img)
            #cv2.waitKey(0)
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    
    def get_flip(self, img):
        return cv2.flip(img, 1)

    def is_match_img(self, res, threshold=0.6):
        return len(np.where(res >= threshold)[0])

    def get_shape(self):
        h, w, *_ = self.img.shape
        return h, w 
    
    def show_img(self, img, description='Show Img func'):
        #img = img or self.img
        #ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
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


    def find_by_template(self, template, deep_search=None, debug=False):
        #cv2.waitKey()
        img_threshold = 0.70
        deep_search = deep_search if deep_search is not None else {}
        res = cv2.matchTemplate(self.gray_img, template.gray_img, cv2.TM_CCOEFF_NORMED) 

        template_flip = self.get_flip(template.gray_img)
        res_flip = cv2.matchTemplate(self.gray_img, template_flip, cv2.TM_CCOEFF_NORMED) 
        def draw_find(res, self, template, threshold=0.5):
            loc = np.where( res >= threshold) 
            if len(loc[0]):
                w, h = template.get_shape() 
                for pt in zip(*loc[::-1]): 
                    image = cv2.rectangle(self.img, pt, (pt[0] + w, pt[1] + h), (168, 64, 165), 2)
                cv2.imshow(f'{self.file_name}', image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print(f'cant detect {self.file_name} in {template.file_name}| in img => {self.file_name}')
            return bool(len(loc[0]))

        matched = self.is_match_img(res, img_threshold)
        #cv2.imshow('hui', template.gray_img)
        #cv2.waitKey(0)
        #cv2.imshow('hui', template_flip)
        #cv2.waitKey(0)
        #cv2.imshow('hui', self.gray_img)
        #cv2.waitKey(0)
        matched_flip = self.is_match_img(res_flip, img_threshold)
                    
        if matched:
            finded = draw_find(res, self, template, img_threshold)
            print(f'i found by img, threshold => {img_threshold} | in img => {self.file_name}')

        if matched_flip:
            finded = draw_find(res_flip, self, template, img_threshold)
            print(f'i found by img_filp and threshold is {img_threshold}| in img => {self.file_name}')
        if not matched:
            #print('hmm i cant find loc, using crop')
            my_threshold = 0.60
            # top and bop half
            def deep_match(where_search_img, what_search_img, deep_search, file_name):
                for method, threshold in deep_search.items():
                    exec(f'data_img = what_search_img.{method}')
                    what_search = locals()['data_img']
                    res_crop = cv2.matchTemplate(where_search_img, what_search, cv2.TM_CCOEFF_NORMED)

                    if self.is_match_img(res_crop, threshold): 
                        draw_find(res_crop, self, template, threshold)
                        print(f'i found by {method} and threshold is {threshold}|for {template.file_name} in img => {file_name}')

            #import ipdb; ipdb.set_trace()
            deep_match(self.gray_img, template, deep_search, self.file_name)
            

        return res






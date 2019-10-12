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


def main():
    #im=ImageGrab.grab(bbox=(0,0, 1290, 1003)) # X1,Y1,X2,Y2
    #im.show()
#    import time 
    #f x in range(30):
        
     #   im=ImageGrab.grab(bbox=(0,0, 1290, 1003)) # X1,Y1,X2,Y2
       # img_name = 'test_save_'+str(x)
      #  img_format = img_name+'.png'
        #im.save(img_format)
        #time.sleep(1)


    img_path = current_path + '\\img\\' + '\\kor_template\\'
    test_gameplay = current_path + '\\img\\' + '\\kor_template\\' + '\\test_like_vid\\'
    hui_list = find('*.png', test_gameplay)
    #print(new_list)
    #print(sorted(hui_list))
    #exit()


#    for image_path in hui_list:
#        opened_img = Cvimage(image_path)
#
#        cv2.imshow('Detected', opened_img.img)
#        cv2.waitKey()
#    print(hui_list)
    search_in_img_filename = 'test_img.jpg'
    search_in_img_path = img_path + search_in_img_filename 

    template_name = 'creep1.png'
    template_path = img_path + template_name

    find_in_img = Cvimage(search_in_img_path)
    #img_rgb = find_in_img.get_img()
    #img_gray = find_in_img.get_img(gray=True) 


    template_base = Cvimage(template_path)
    #template_img = template_base.get_img(gray=True)
    #template = template_base.make_flip() 
    #import ipdb; ipdb.set_trace()
    #temp_gray_img = template_base.get_gray_img()
    #top, bot = template_base.half_crop_img(temp_gray_img)
    
    #template_base.show_img(template_base.img)

    #find_in_img.find_by_template(template, debug=True)
    for find_in_img_path in hui_list:
        find_in_img = Cvimage(find_in_img_path)
        find_in_img.find_by_template(template_base, debug=True)
#    w, h = template_base.get_shape() 
#    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED) 
#    threshold = 0.7
#    loc = np.where( res >= threshold) 
#
#    #import ipdb; ipdb.set_trace()
#    for pt in zip(*loc[::-1]): 
#        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (168, 64, 165), 2)
#        
#    cv2.imshow('Detected', img_rgb)
#    cv2.waitKey()
#    import ipdb; ipdb.set_trace()


 #   template = cv2.imread("2019-07-02_06-55_1.png", cv2.IMREAD_GRAYSCALE)

if __name__ == "__main__":

    main()

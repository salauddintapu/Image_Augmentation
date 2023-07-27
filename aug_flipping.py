import os
import numpy as np
import cv2
from tqdm import tqdm
from imageio import mimread


#flipping image about the x-axis/horizontally
def horizontal_flip(img):
    h_img = cv2.flip(img, 0)
    return h_img


#flipping image about the y-axis/vertically
def vertical_flip(img):
    v_img = cv2.flip(img, 1)
    return v_img


#flipping image about both axis
def invert(img):
    hv_img = cv2.flip(img, -1)
    return hv_img


#read and write images
def read(path, files, write_path = None, gif=False):
    if write_path == None:
        os.mkdir('./aug_data')
        write_path = os.getcwd() + '/aug_data/'
        print(f'No argument for write_path has been passed. Augmented images will exported to default {write_path}')
    
    
    #read GIF extension image file
    if gif:
        for file in tqdm(files):
            f = mimread(path + file)
            for img in f:
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                img = img.resize(img, (512, 512))           #resizes images as 512 X 512 pixels
                h_img = horizontal_flip(img)
                cv2.imwrite(f'hori_{write_path+file[:-4]}.png', h_img)
                v_img = vertical_flip(img)
                cv2.imwrite(f'verti_{write_path+file[:-4]}.png', v_img)
                i_img = invert(img)
                cv2.imwrite(f'inv_{write_path+file[:-4]}.png', i_img)
    
    else:
        for file in tqdm(files):
            img = cv2.imread(path+file)
            img = cv2.resize(img, (512, 512))           #resizes images as 512 X 512 pixels
            h_img = horizontal_flip(img)
            cv2.imwrite(f'{write_path}h_{file[:-4]}.png', h_img)
            v_img = vertical_flip(img)
            cv2.imwrite(f'{write_path}v_{file[:-4]}.png', v_img)
            i_img = invert(img)
            cv2.imwrite(f'{write_path}inv_{file[:-4]}.png', i_img)

path = ('DRIVE/training/images/')
files = sorted(os.listdir('DRIVE/training/images/'))
read(path, files)
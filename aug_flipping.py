import os
import cv2
from tqdm import tqdm

class FLIP():
    def augmentation(self, img, file, save_path):
        try:    
            #horizontal flip
            h_img = cv2.flip(img, 0)
            cv2.imwrite(f'{save_path}/h_{file[:-4]}.png', h_img)
            #vertical flip
            v_img = cv2.flip(img, 1)
            cv2.imwrite(f'{save_path}/v_{file[:-4]}.png', v_img)
            #inverted
            inv_img = cv2.flip(img, -1)
            cv2.imwrite(f'{save_path}/inv_{file[:-4]}.png', inv_img)
        except Exception as e:
            print(e)

    def read(self, path, files, save_path='aug_data'):
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        for file in tqdm(files):
            img = cv2.imread(path+file)
            img = cv2.resize(img, (512, 512))           #resizes images as 512 X 512 pixels
            self.augmentation(img=img, file=file, save_path=save_path)

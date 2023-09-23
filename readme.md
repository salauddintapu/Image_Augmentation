# Image_Augmentation
<br>
Provide the path of the directory and the files as Pathlike object (os.listdir). The **FLIP** class will perform horizontal and vertical flip, and finally invert the image.

**Example:**
import os
from aug_flipping import FLIP
flip = FLIP()

path = './images/'
files = sorted(os.listdir(path))

flip.read(path=path, files=files, save_path='output')
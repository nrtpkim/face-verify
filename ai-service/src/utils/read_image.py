import cv2
import io
from PIL import Image
import numpy as np

def read_image(img_path="assets/photo/unnamed.jpg"):

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def read_img_from_bytes(bytes):
    image = Image.open(io.BytesIO(bytes))
    image_np = np.array(image)

    return image_np
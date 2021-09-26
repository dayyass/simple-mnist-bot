import io

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image


def preprocess_image(file):
    img = np.array(Image.open(io.BytesIO(file)).convert("L")).astype("float32") / 255
    img = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_AREA)
    img = img[np.newaxis, :, :, np.newaxis]
    img = tf.convert_to_tensor(img)

    return img


def inference(model, img):
    logits = model(img)
    cls = logits.numpy()[0].argmax()

    return cls

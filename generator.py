import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
from tensorflow.config.experimental import list_physical_devices, set_memory_growth
import numpy as np
import cv2
import time

gpus=list_physical_devices('GPU')
for gpu in gpus:
    set_memory_growth(gpu, True)

model=load_model("models/gen8.h5", compile=False)

while True:
    try:
        n=int(input("Generate number (0-9) (any other number to exit) : "))
    except:
        print("Wrong input")
        continue
    if n<0 or n>9:
        break
    label=np.zeros(shape=(1, 10))
    label[0,n]=1
    latent=np.random.random(size=(1,100))
    p=model.predict([latent,label])
    img=p[0].reshape(28,28)
    cv2.imshow(str(n),img)
    _ = cv2.waitKey(0)
    cv2.destroyAllWindows()
    n=input("Save the image (in current directory)?(y/n) : ")
    if n.lower() == 'y':
        cv2.imwrite("%d.jpg"%time.time(), img)
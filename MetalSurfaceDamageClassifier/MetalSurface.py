import numpy as np
from keras.models import load_model
import cv2



model=load_model("Metal_image_Damage_Identifier.keras")


img=cv2.imread("Metal Surface Detector/test/Crazing/cr_1.bmp")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
img = cv2.resize(img, (224,224))
img = img / 255.0

img = np.expand_dims(img, axis=0)  

pred = model.predict(img)

pred_class = np.argmax(pred, axis=1)[0]
print("Predicted class:", pred_class) # ['Crazing', 'Inclusion', 'Patches', 'Pitted', 'Rolled', 'Scratches']

match pred_class:
    case 0:
        print("Crazing")

    case 1:
        print("Inclusion")

    case 2:
        print("Patches")


    case 3:
        print("Pitted")


    case 4:
        print("Rolled")


    case 5:
        print("Scratches")                    


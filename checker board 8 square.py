import numpy as np
import cv2
b = np.ones([480,480],dtype='uint8')*255
for i in range(60,480,60*2):
        for jin range(60,480,60*2):

           b[j-60:j,i-60:i] = 0
           b[j:j+60,i:i+60] = 0
cv2.imshow(' checkerboard 8 square',b)
cv2.waitKey(0)
cv2.destroyAllWindows() 

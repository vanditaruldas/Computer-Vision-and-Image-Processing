import cv2
import numpy as np

filename = 'test.jpg'
img = cv2.imread(filename)
dst = np.zeros((img.shape[0],img.shape[1]))
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
dst = cv2.pyrMeanShiftFiltering(img,16,32,dst,0,term_crit)
cv2.imshow('dst',dst)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
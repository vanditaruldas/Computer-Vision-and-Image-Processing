import cv2,numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

img = cv2.imread('lena_gray.jpg',0);

#Problem (2) : Histogram Equalization
eimg = deepcopy(img)
h = np.zeros(256)
ch = np.zeros(256)
eh = np.zeros(256)
ech = np.zeros(256)
t = np.zeros(256)
temp=(255.0)/(img.shape[0]*img.shape[1])

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        h[img[i][j]]+=1
        
sum = 0;
for i in range(256):
    sum+=h[i]
    ch[i]=sum
    t[i]=round(temp*ch[i])
    
for i in range(eimg.shape[0]):
    for j in range(eimg.shape[1]):
        eimg[i][j]=t[eimg[i][j]]
        
for i in range(eimg.shape[0]):
    for j in range(eimg.shape[1]):
        eh[eimg[i][j]]+=1
        
sum = 0;
for i in range(256):
    sum+=eh[i]
    ech[i]=sum
        
x_pos = np.arange(256)
plt.figure(1) 
plt.bar(x_pos, h, align='center', alpha=0.5)
plt.xticks(np.arange(0, 256, 10.0))
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Historgram of Original Image')
plt.figure(2) 
plt.bar(x_pos, ch, align='center', alpha=0.5)
plt.xticks(np.arange(0, 256, 10.0))
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Cumulative Historgram of Original Image')
plt.figure(3) 
plt.bar(x_pos, eh, align='center', alpha=0.5)
plt.xticks(np.arange(0, 256, 10.0))
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Historgram of Enhanced Image')
plt.figure(4) 
plt.bar(x_pos, ech, align='center', alpha=0.5)
plt.xticks(np.arange(0, 256, 10.0))
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Cumulative Historgram of Enhanced Image')
plt.show()

cv2.imshow("Original Image",img);
cv2.imshow("Enhanced Image",eimg);
cv2.waitKey(0);
cv2.destroyAllWindows();
import cv2,numpy as np

img1 = cv2.imread('view1.png')
img5 = cv2.imread('view5.png')
disp1 = cv2.imread('disp1.png',0)
disp5 = cv2.imread('disp5.png',0)

img3 = np.zeros((img1.shape[0],img1.shape[1],img1.shape[2]))
dsp = np.full((img1.shape[0],img1.shape[1]),-1)

disp1 = disp1/2
disp5 = disp5/2

for i in range(0,disp1.shape[0]):
    for j in range(0,disp1.shape[1]):
        temp = j-disp1[i][j]
        if(temp>=0):
            if(dsp[i][temp]<disp1[i][j]):
                dsp[i][temp]=disp1[i][j]
                img3[i][temp]=img1[i][j]
                
for i in range(0,disp5.shape[0]):
    for j in range(0,disp5.shape[1]):
        temp = j+disp5[i][j]
        if(temp<disp5.shape[1]):
            if(dsp[i][temp]<disp5[i][j]):
                dsp[i][temp]=disp5[i][j]
                img3[i][temp]=img5[i][j]
                
cv2.imwrite('view3gen.jpg',img3) 
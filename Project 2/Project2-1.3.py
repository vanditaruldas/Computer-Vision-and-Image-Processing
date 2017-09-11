import cv2
import numpy as np

img1 = cv2.imread('view1.png',0)
img5 = cv2.imread('view5.png',0)

OcclusionCost = 20

disparitymatrix = np.zeros((img1.shape[0],img1.shape[1]))

for line in range(img1.shape[0]):    
    row = img1[line]
    col = img5[line]
    cost = np.zeros((img1.shape[1]+1,img5.shape[1]+1))
    direction = np.zeros((img1.shape[1]+1,img5.shape[1]+1))

    for i in range(cost.shape[0]):
        cost[i][0]=i*OcclusionCost
    
    for i in range(cost.shape[1]):
        cost[0][i]=i*OcclusionCost
        
    for i in range(1,cost.shape[0]):
        for j in range(1,cost.shape[1]):
            min1=cost[i-1][j-1]+(abs(row[i-1]-col[j-1]))
            min2=cost[i-1][j]+OcclusionCost
            min3=cost[i][j-1]+OcclusionCost
            a = np.array([min1,min2,min3])
            cost[i][j]=np.min(a)
            direction[i][j]=np.argmin(a)+1
            
    p=direction.shape[0]-1
    q=direction.shape[1]-1
    while((p!=0) and (q!=0)):
        temp = direction[p][q]
        if(temp == 1):
            disparitymatrix[line][p-1]=abs(p-q)
            p-=1
            q-=1
        elif(temp == 2):
            p-=1
        else:
            q-=1
            
cv2.imwrite('disparitymatrix.jpg',disparitymatrix) 
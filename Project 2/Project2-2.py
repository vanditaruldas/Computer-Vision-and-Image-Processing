import cv2,numpy as np

img = cv2.imread('Butterfly.jpg');
dst = np.zeros((img.shape[0]*img.shape[1],5))
msimg = np.zeros((img.shape[0],img.shape[1],img.shape[2]))

count = 0
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        dst[count]=np.array([img[i][j][0],img[i][j][1],img[i][j][2],i,j])
        count+=1

base = np.array([])  
h=60
iter=10     
while(dst.size!=0):
    if(base.size == 0):
        base = dst[0]
        
    sum = np.zeros(5)
    count = 0
    matches = []
    for i in range(0,dst.shape[0]):
        eqdst = np.sqrt(np.sum(np.square(base-dst[i])))
        if(eqdst<=h):
            matches.append(i)
            sum+=dst[i]
            count+=1
            
    sum/=count
    iterdst = np.sqrt(np.sum(np.square(base-sum)))
    if(iterdst<=iter):
        for j in range(0,len(matches)):
            temp = dst[matches[j]]
            msimg[temp[3]][temp[4]] = np.array([sum[0],sum[1],sum[2]])          
        dst =np.delete(dst,matches,0)
        base = np.array([])
    else:
        base = sum
                
cv2.imwrite('msimg.jpg',msimg) 
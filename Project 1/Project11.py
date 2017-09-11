import cv2,numpy as np

img = cv2.imread('lena_gray.jpg',0);

#Problem (1) : 1D and 2D Convolution on Images
paddedimg = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_REPLICATE)
gx = np.zeros((paddedimg.shape[0],paddedimg.shape[1]))
gy = np.zeros((paddedimg.shape[0],paddedimg.shape[1]))
gx1d = np.zeros((paddedimg.shape[0],paddedimg.shape[1]))
gy1d = np.zeros((paddedimg.shape[0],paddedimg.shape[1]))
g = np.zeros((paddedimg.shape[0],paddedimg.shape[1]))
sf1 = np.array([-1,0,1])
sf2 = np.array([[1],[2],[1]])
sf3 = np.array([1,2,1])
sf4 = np.array([[-1],[0],[1]])
for i in range(1,paddedimg.shape[0]-1):
    for j in range(1,paddedimg.shape[1]-1):
        gx[i][j] = (paddedimg[i-1][j-1]*-1)+(paddedimg[i-1][j+1]*1)+(paddedimg[i][j-1]*-2)+(paddedimg[i][j+1]*2)+(paddedimg[i+1][j+1]*-1)+(paddedimg[i+1][j+1]*1)
        gy[i][j] = (paddedimg[i-1][j-1]*-1)+(paddedimg[i-1][j]*-2)+(paddedimg[i-1][j+1]*-1)+(paddedimg[i+1][j-1]*1)+(paddedimg[i+1][j]*2)+(paddedimg[i+1][j+1]*1)
        gx1d[i][j] = np.sum((paddedimg[i-1:i+2,j-1:j+2]*sf1)*sf2)
        gy1d[i][j] = np.sum((paddedimg[i-1:i+2,j-1:j+2]*sf3)*sf4)
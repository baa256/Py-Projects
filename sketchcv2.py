import cv2


#read 
img = cv2.imread('jl.jpg')

# grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# negative
#inverting the grayscale value of every pixel 

img_gray_inv = 255 - img_gray


# gaussian blur , good to reduce noise and detail ( smoothing )

img_blur = cv2.GaussianBlur(img_gray_inv , ksize = (21,21),
                            sigmaX = 0 , sigmaY = 0 )



cv2.imshow('image' , img_blur)
cv2.waitKey(0)
cv2.destoryAllWindows()

cv2.imwrite('sketch.jpg, img_blur')


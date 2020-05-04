import cv2

img=cv2.imread("HappyFish.jpg",1)

print(img)



cv2.imshow('fish',img)
k=cv2.waitKey(0)


if k==5:
    destroyAllWindows()
if k==ord("s"):
    cv2.imwrite('fish2.png',img)
    cv2.destroyAllWindows()

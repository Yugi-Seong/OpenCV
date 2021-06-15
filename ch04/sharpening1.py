import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


blr = cv2.GaussianBlur(src, (0, 0), 2)
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)

blr = cv2.GaussianBlur(src, (0, 0), 2)
src_f = src.astype(np.float32)

blr = cv2.GaussianBlur(src_f, (0, 0), 2)
dstf = np.clip(2.0*src_f - blr, 0, 255).astype(np.uint8)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dstf', dstf)

cv2.waitKey()

cv2.destroyAllWindows()

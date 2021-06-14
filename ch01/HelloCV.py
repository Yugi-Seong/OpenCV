# 고양이사진(cat.bmp파일)을 여는 코드
import cv2
import sys

print('Hello OpenCV', cv2.__version__)
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) # cat.bmp파일을 불러와 img 변수(array형태)에 저장 

if img is None :  # 영상 파일 불러오기 실패하면 에러 메세지를 출력하고 종료  
    print("Image load failed~!!")
    sys.exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 창조절 가능 
# cv2.moveWindow('image', 500,500) # 창 위치이동
cv2.imshow('image',img)
# cv2.imwrite('catzz.png',img)  # catzz.png 이름으로 이미지 저장 

cv2.waitKey(3000)  # 3초 후 자동 꺼짐 
while True:
    if cv2.waitKey() == ord('q'):  # q누를 경우 자동 꺼짐 
        break

cv2.destroyAllWindows() # 생성된 모든 창을 닫음/

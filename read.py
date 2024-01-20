import cv2 as cv
# img=cv.imread('cat.jpeg')
# resized_img = cv.resize(img, (0, 0), fx=0.25, fy=0.25)
# cv.imshow('cat',resized_img)
# cv.waitKey(0)
def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
capture = cv.VideoCapture('cat.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleframe(frame,scale=0.75)
    cv.imshow('video_resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release
cv.destroyAllWindows()


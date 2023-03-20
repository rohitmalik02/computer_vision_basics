import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # works only for live capture/videos
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread("Photos/cat_large.jpg")
cv.imshow('Cat', rescaleFrame(img, scale=0.2))
cv.waitKey(0)

capture = cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', rescaleFrame(frame, scale=0.8))
    if (cv.waitKey(17) & 0xFF == ord('d')):
        break

capture.release()
cv.destroyAllWindows()

# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', rescaleFrame(frame))
#     if (cv.waitKey(17) & 0xFF == ord('d')):
#         break

# capture.release()
# cv.destroyAllWindows()

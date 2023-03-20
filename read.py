import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# print(bin(cv.waitKey(0)))

capture = cv.VideoCapture("Videos/dog.mp4")
# VideoCapture(src) set it to 0 for default webcam and successive integers for
# other capture devices. Else enter path to the video
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

# while true, capture frames, wait for 17ms for a keypress
# if key pressed and it's "d", quit! else capture next frame
# changing to waitkey(1000) will mean capturing one frame per second
# as the code waits for a second before moving on to capture the next frame
# waitKey(0) waits indefinitely for a key press, hence used for stil images
# waitkey(17) for 60 fps, waitKey(33) for 30 fps
    if (cv.waitKey(17) & 0xFF == ord('d')):
        break

# cv.waitKey returns a 32 bit integer representing the ascii code of the
# pressed key. 0xFF is an 8 bit mask which when bitwise 'and'-ed with the 32 bit
# integer makes the first 24 bits 0 leaving behind the 8 bit ascii code of the
# pressed key. Here 'd' was chosen as the 'to quit' key. ord('d') will return
# ascii code of 'd' (100).

capture.release()
cv.destroyAllWindows()

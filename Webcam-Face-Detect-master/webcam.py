import cv2
import sys

cascPath_face   = "haarcascade_frontalface_default.xml"
cascPath_eye    = "haarcascade_eye.xml"
faceCascade = cv2.CascadeClassifier(cascPath_face)
eyeCascade  = cv2.CascadeClassifier(cascPath_eye)


video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    """
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    """

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) 

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray    = gray[y:y+h, x:x+w]
        roi_color   = img[y:y+h, x:x+w]
        eyes        = eyeCascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
    # Display the resulting frame
    #cv2.imshow('Video', frame)
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

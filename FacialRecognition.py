import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)



while True:
    check, img = video.read()
    cv2.putText(img, 'Facial Recognition', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), thickness = 2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    fps = video.get(cv2.CAP_PROP_FPS)
    cv2.putText(img, 'FPS: ' + str(fps), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), thickness = 2)
    if len(faces) == 0:
        cv2.putText(img, 'No Face Detected', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), thickness = 2)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)
        cv2.putText(img, 'Face Detected', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), thickness = 2)
        
        if len(faces) == 1:
            cv2.putText(img, 'One Face Detected', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), thickness = 2)
        elif len(faces) > 1:
            cv2.putText(img, str(len(faces)) + ' Faces Detected', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), thickness = 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('image.jpg', img)
        break


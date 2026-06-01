import cv2
import face_recognition
import numpy as np



video = cv2.VideoCapture(0)

aurick_image = face_recognition.load_image_file("aurick.jpg")
aurick_encoding = face_recognition.face_encodings(aurick_image)[0]

lebron_image = face_recognition.load_image_file("lebron.png")
lebron_encoding = face_recognition.face_encodings(lebron_image)[0]

known_face_encodings = [aurick_encoding, lebron_encoding]
known_face_names = ["Aurick", "LeBron"]



while True:
    check, img = video.read()
    if check == False:
        break
    
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cap = video.get(cv2.CAP_PROP_FPS)
    cv2.putText(img, f"FPS: {cap:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

    if len(face_locations) == 0:
        cv2.putText(img, "No faces detected", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    elif len(face_locations) == 1:
        cv2.putText(img, "One face detected", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    else:
        cv2.putText(img, f"{str(len(face_locations))} faces detected", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
        name = "Unknown"
        matches = face_recognition.compare_faces(known_face_encodings, encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index] == True:
            name = known_face_names[best_match_index]

        cv2.rectangle(img, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(img, name, (left, top - 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Face Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("saved_image.jpg", img)
        print("Image saved as saved_image.jpg")
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

       

video.release()
cv2.destroyAllWindows()

  


    


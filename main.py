import face_recognition
import cv2
import numpy as np
import pyttsx3
# from image_loader import *

# TODO
# RPi, ImageLoader

engine = pyttsx3.init()

video_capture = cv2.VideoCapture(0)

anirban_image = face_recognition.load_image_file("images/anirban.jpg")
anirban_face_encoding = face_recognition.face_encodings(anirban_image)[0]

shilpi_image = face_recognition.load_image_file("images/shilpi.jpg")
shilpi_face_encoding = face_recognition.face_encodings(shilpi_image)[0]

borshuen_image = face_recognition.load_image_file("images/bor-shuen.jpg")
borshuen_face_encoding = face_recognition.face_encodings(borshuen_image)[0]

dhananjay_image = face_recognition.load_image_file("images/dhananjay.jpg")
dhananjay_face_encoding = face_recognition.face_encodings(dhananjay_image)[0]

jayson_image = face_recognition.load_image_file("images/jayson.jpg")
jayson_face_encoding = face_recognition.face_encodings(jayson_image)[0]

anshi_image = face_recognition.load_image_file("images/anshi.jpg")
anshi_face_encoding = face_recognition.face_encodings(anshi_image)[0]

ainesh_image = face_recognition.load_image_file("images/ainesh.jpg")
ainesh_face_encoding = face_recognition.face_encodings(ainesh_image)[0]

astrid_image = face_recognition.load_image_file("images/astrid.jpg")
astrid_face_encoding = face_recognition.face_encodings(astrid_image)[0]

tillman_image = face_recognition.load_image_file("images/tillman.jpg")
tillman_face_encoding = face_recognition.face_encodings(tillman_image)[0]

matthew_image = face_recognition.load_image_file("images/matthew.jpg")
matthew_face_encoding = face_recognition.face_encodings(matthew_image)[0]

shikha_image = face_recognition.load_image_file("images/shikha.jpg")
shikha_face_encoding = face_recognition.face_encodings(shikha_image)[0]

known_face_encodings = [
    anirban_face_encoding,
    shilpi_face_encoding,
    borshuen_face_encoding,
    dhananjay_face_encoding,
    jayson_face_encoding,
    anshi_face_encoding,
    ainesh_face_encoding,
    astrid_face_encoding,
    tillman_face_encoding,
    matthew_face_encoding,
    shikha_face_encoding
]

known_face_names = [
    "Anirban",
    "Shilpi",
    "Bor-Shuen",
    "Dhananjay",
    "Jayson",
    "Anshi",
    "Ainesh",
    "Astrid",
    "Tillman",
    "Matthew",
    "Shikha"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    
    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        rgb_small_frame = small_frame[:, :, ::-1]
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            face_names.append(name)
            
            if cv2.waitKey(1) & 0xFF == ord('s'):
                engine.say(name)
                engine.runAndWait()

        
    process_this_frame = not process_this_frame
    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()
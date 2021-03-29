import cv2
import numpy as np
import face_recognition
import os

# path = 'source'
# images = []
# Names = []
# myList = os.listdir(path)
# print(myList)
#
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     Names.append(os.path.splitext(cl)[0])
# print(Names)
#
#
# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList
#
# encodeListknown = findEncodings(images)
# print("Encoding Complete")

img1 = face_recognition.load_image_file("source/elon musk.jpeg")
img2 = face_recognition.load_image_file("source/bill gates.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

faceLocation = face_recognition.face_locations(img1)[0]
faceEncoding = face_recognition.face_encodings(img1)[0]
cv2.rectangle(img1, (faceLocation[3],faceLocation[0]), (faceLocation[1],faceLocation[2]), (255,0,255), 2) 

faceLocation1 = face_recognition.face_locations(img2)[0]
faceEncoding1 = face_recognition.face_encodings(img2)[0]
cv2.rectangle(img2, (faceLocation1[3],faceLocation1[0]), (faceLocation1[1],faceLocation1[2]), (255,255,0), 4)


results = face_recognition.compare_faces([faceEncoding],faceEncoding1)
faceDistance = face_recognition.face_distance([faceEncoding],faceEncoding1)
print(results, faceDistance)
cv2.putText(img2, f'{results} {round(faceDistance[0], 2)}',(100, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,255,0), 3)

cv2.imshow('Bill Gates', img1)
cv2.imshow('Bill Gates1', img2)
cv2.waitKey(0)

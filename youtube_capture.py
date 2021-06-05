
import cv2
import pafy

url = "https://www.youtube.com/watch?v=7tvQya78w7g"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture(best.url)
 
count = 0

while True:
    ret, image = capture.read()
    cv2.imshow('image',image)
    cv2.waitKey(1)
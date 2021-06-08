
import cv2
import pafy


def video_info(cap):
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
 
    print('length : ', length)
    print('width : ', width)
    print('height : ', height)
    print('fps : ', fps)

    return fps, length

url = "https://www.youtube.com/watch?v=CMqROal8Usk"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture(best.url)
fps, length=video_info(capture)

saved_path='./image/'
count = 0

print(url)
# while True:
while(capture.isOpened()):
    ret, image = capture.read()
    
    if cv2.waitKey(1) == ord(' '):
        image = cv2.resize(image, dsize=(640, 640), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite("{0}{1}_{2}.jpg".format(saved_path,url[-4:],count), image)
        count += 1

    if cv2.waitKey(1) == ord('q'):
        capture.release()
        break

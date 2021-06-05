
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

url = "https://www.youtube.com/watch?v=mi_zTNkcBrc"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture(best.url)
fps, length=video_info(capture)

saved_path='./image/'
count = 0
time = 0.7

# while True:
while(capture.isOpened()):
    ret, image = capture.read()
    # cv2.imshow('image',image)
    if(int(capture.get(1)) % int(fps) == 0):
        print('Saved frame number : ' + str(int(capture.get(1))))
        image = cv2.resize(image, dsize=(640, 640), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite("{0}{1}_{2}.jpg".format(saved_path,url[-4:],count), image)
        print('Saved frame%d.jpg' % count)
        count += 1

    if(int(capture.get(1)) >= length):
        capture.release()
        break
    # if cv2.waitKey(time) == ord('c'):
    #     print("chal kak")
    #     capture.release()
    #     break

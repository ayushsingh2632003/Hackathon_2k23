# opening  camera
import cv2
import subprocess
import mediapipe as mp
import pyautogui
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)
#done

while True:
    _, frame = cap.read()

    frame = cv2.flip(frame,1) #1 is for y axis flip
    frame_height,frame_width, _ =frame.shape
    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    output =hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    index_y=0
    index_x=0
    if hands:
        for hand in hands:

            drawing_utils.draw_landmarks(frame, hand)
            landmarks=hand.landmark
            for id , landmark in enumerate(landmarks):

                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if(id==8 ):
                    cv2.circle(img=frame , center=(x,y),radius =10, color=(0,235,255))
                    index_x = screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)

                if (id == 4):
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 235, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                   # print('outside',abs(index_y-thumb_y))


                    if abs(index_y-thumb_y) < 80:
                        pyautogui.click()
                        pyautogui.sleep(1)



                if(id==5):
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 235, 255))
                    f_xx = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    print("new",abs(index_x-f_xx))
                    if abs(index_x-f_xx)<80:
                        file = subprocess.Popen("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")


                if (id==12):
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 235, 255))
                    f_x = screen_width / frame_width * x
                    f_y = screen_height / frame_height * y

                   # print("new ",abs(index_x-f_x))



                    if abs(index_x-f_x)>400:
                        exit()


    cv2.imshow("virtual mouse", frame)
    cv2.waitKey(1)




import cv2
import mediapipe as mp
import math
import numpy as np
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol, volBar, volPer = volRange[0], volRange[1], 400, 0

wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)

volume_paused = False  
pause_start_time = None  
pause_duration = 1  
last_volume = volume.GetMasterVolumeLevel()  
tracking_active = True 

thumbs_down_start_time = None 
thumbs_down_duration = 4 


message = None
message_start_time = None  
message_duration = 1  

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cam.isOpened():
        success, image = cam.read()
        if not success:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        
        
        if results.multi_hand_landmarks and tracking_active:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

            
            lmList = []
            myHand = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            # Calculate distance between thumb and index finger
            if len(lmList) != 0:
                x1, y1 = lmList[4][1], lmList[4][2]  
                x2, y2 = lmList[8][1], lmList[8][2]  

                # Draw circles and line
                cv2.circle(image, (x1, y1), 15, (255, 255, 255))
                cv2.circle(image, (x2, y2), 15, (255, 255, 255))
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

                
                length = math.hypot(x2 - x1, y2 - y1)

           
                if not volume_paused:
                    vol = np.interp(length, [50, 220], [minVol, maxVol])
                    volume.SetMasterVolumeLevel(vol, None)
                    last_volume = vol  # Update the last volume level
                    volBar = np.interp(length, [50, 220], [400, 150])
                    volPer = np.interp(length, [50, 220], [0, 100])
                    pause_start_time = time.time()
                    volume_paused = True

      
        if volume_paused:
            elapsed_time = time.time() - pause_start_time
            remaining_time = max(0, pause_duration - elapsed_time)  

            cv2.putText(image, f'Pausing: {int(remaining_time)}s', (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

            if elapsed_time >= pause_duration:
                volume_paused = False 

        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]
            thumb_tip = myHand.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = myHand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = myHand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = myHand.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = myHand.landmark[mp_hands.HandLandmark.PINKY_TIP]

            if thumb_tip.y < index_tip.y and thumb_tip.y < middle_tip.y and thumb_tip.y < ring_tip.y and thumb_tip.y < pinky_tip.y:
                if tracking_active:  
                    tracking_active = False 
                    message = "Voice is Perfect. Tracking Stopped"
                    message_start_time = time.time()

            # Thumbs Down: Thumb is below other fingers
            elif thumb_tip.y > index_tip.y and thumb_tip.y > middle_tip.y and thumb_tip.y > ring_tip.y and thumb_tip.y > pinky_tip.y:
                if thumbs_down_start_time is None:
                    thumbs_down_start_time = time.time()
                else:
                    elapsed_time = time.time() - thumbs_down_start_time
                    remaining_time = max(0, thumbs_down_duration - elapsed_time) 
                    cv2.putText(image, f'Thumbs Down: {int(remaining_time)}s', (50, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    if elapsed_time >= thumbs_down_duration:
                        if not tracking_active:  
                            tracking_active = True  
                            message = "Voice is Not Perfect. Tracking Started"
                            message_start_time = time.time()
            else:
                thumbs_down_start_time = None  

        
        if message is not None and message_start_time is not None:
            elapsed_time = time.time() - message_start_time
            if elapsed_time <= message_duration:
                cv2.putText(image, message, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            else:
                message = None  

        
        cv2.rectangle(image, (50, 150), (85, 400), (0, 0, 0), 3)
        cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 0, 0), cv2.FILLED)
        cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

        cv2.imshow('Hand Detector', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cam.release()
cv2.destroyAllWindows()
import cv2
import socket
from cvzone.HandTrackingModule import HandDetector
w,h=1280,720

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, w)
cap.set(4, h)

det= HandDetector(maxHands=1,detectionCon=0.8)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sap = ("127.0.0.1",5052)
while True:
    data=[]
    success, img = cap.read(0)
    hands, img = det.findHands(img, flipType=True)
    if hands:
        hand=hands[0]
        lmList=hand['lmList']
        bbox1 = hand["bbox"]
        cp= hand["center"]
        handtype= hand["type"]
        # print(det.fingersUp(hand))
        if(det.fingersUp(hand)[0]==1 and  det.fingersUp(hand)[1]==1 and  det.fingersUp(hand)[2]==1 and  det.fingersUp(hand)[3]==1and  det.fingersUp(hand)[4]==1):
            print("hi")

        if(det.fingersUp(hand)[0]==0 and  det.fingersUp(hand)[1]==1 and  det.fingersUp(hand)[2]==1 and  det.fingersUp(hand)[3]==0and  det.fingersUp(hand)[4]==0):
            print("Peace")
        if (det.fingersUp(hand)[0] == 0 and det.fingersUp(hand)[1] == 1 and det.fingersUp(hand)[2] == 1 and
                    det.fingersUp(hand)[3] == 0 and det.fingersUp(hand)[4] == 0):
                print("Peace")

        # print(bbox1)
        # print(lmList)
        for lm in lmList:
            data.extend([lm[0],h - lm[1],lm[2]])
            # print(data)
        s.sendto(str.encode(str(data)), sap)
    img= cv2.resize(img,(0,0),None,0.5,0.5)

    cv2.imshow("Image", img)
    cv2.waitKey(1);

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #  break
# cv2.destroyAllWindows()
# After the loop release the cap object
# cap.release()
# Destroy all the windows

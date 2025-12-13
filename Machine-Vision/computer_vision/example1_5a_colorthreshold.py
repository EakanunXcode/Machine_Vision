import numpy as np
import cv2

cap = cv2.VideoCapture(0)

TARGET_SIZE = (640,360)

while(True):
    ret,im = cap.read()
    im_resized = cv2.resize(im, TARGET_SIZE)
    im_flipped = cv2.flip(im_resized, 1)    

    # ---------- 1. ส่วนเดิม (Coke - สีแดง) ----------
    mask = cv2.inRange(im_flipped,(0,0,90),(50,50,255)) #(r,g,b) -> จริงๆคือ (b,g,r)

    cv2.imshow('mask', mask) # หน้าต่าง mask นี้จะโชว์แค่ของ Coke ตามโค้ดเดิม
    cv2.moveWindow('mask',TARGET_SIZE[0],0)

    print(np.sum(mask/255))

    if(np.sum(mask/255) > 10000):
        cv2.putText(im_flipped,'Coke',(50,100),
                    fontFace = cv2.FONT_HERSHEY_PLAIN,
                    fontScale = 5,
                    thickness = 3,
                    color = (0,0,255))         

    # ---------- 2. ส่วนที่เพิ่ม (Pepsi - สีน้ำเงิน) ----------
    # เน้นค่า B สูงๆ (ตัวแรก), ค่า G กับ R ต่ำๆ
    mask_pepsi = cv2.inRange(im_flipped,(90,0,0),(255,80,80)) 
    
    if(np.sum(mask_pepsi/255) > 10000):
        cv2.putText(im_flipped,'Pepsi',(50,200), # ขยับตำแหน่งลงมาเป็น 200
                    fontFace = cv2.FONT_HERSHEY_PLAIN,
                    fontScale = 5,
                    thickness = 3,
                    color = (255,0,0)) # สีตัวหนังสือเป็นน้ำเงิน (B,G,R)

    # ---------- 3. ส่วนที่เพิ่ม (Sprite - สีเขียว) ----------
    # เน้นค่า G สูงๆ (ตัวกลาง), ค่า B กับ R ต่ำๆ
    mask_sprite = cv2.inRange(im_flipped,(0,90,0),(80,255,80))

    if(np.sum(mask_sprite/255) > 10000):
        cv2.putText(im_flipped,'Sprite',(50,300), # ขยับตำแหน่งลงมาเป็น 300
                    fontFace = cv2.FONT_HERSHEY_PLAIN,
                    fontScale = 5,
                    thickness = 3,
                    color = (0,255,0)) # สีตัวหนังสือเป็นเขียว (B,G,R)

    # ----------------------------------------------------

    cv2.imshow('camera', im_flipped)
    cv2.moveWindow('camera',0,0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
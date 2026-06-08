import cv2
cap = cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier(r'D:\CODING\OPENCV\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'D:\CODING\OPENCV\haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(r'D:\CODING\OPENCV\haarcascade_smile.xml')
while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)
        roi_eye = gray[y:y+h,x:x+w]
        roi_smile = gray[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_eye,1.3,10)
        smile = smile_cascade.detectMultiScale(roi_smile,1.2,5)
        if len(eyes)>0:
            cv2.putText(img=frame,text="eyes detected",fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,thickness=2,org=(x,y-30),color=(0,255,0))
        if len(smile)>0:
            cv2.putText(img=frame,text="smile detected",fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,thickness=2,org=(x,y-10),color=(0,255,0)) 
    cv2.imshow('smart_face_detection',frame)    
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break
cap.release()
cv2.destroyAllWindows()           

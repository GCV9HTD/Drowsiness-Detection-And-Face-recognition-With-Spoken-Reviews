# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IBMProject.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import speech_recognition as sr
import imutils
import ibm_db
import time
import face_recognition
import pickle
import dlib
import cv2
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='<api-key-here>',
    url='<url-here>'
)
dsn_hostname = "" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = ""        # e.g. "abc12345"
dsn_pwd = ""      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "50000"                # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(320, 20, 141, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 50, 141, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(300, 110, 241, 91))
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 200, 91, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(150, 190, 371, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 91, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 230, 631, 61))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 340, 101, 21))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 101, 21))
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 340, 191, 21))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(150, 381, 191, 20))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 420, 101, 16))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(150, 420, 191, 21))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 340, 291, 91))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        self.menuMENU_2 = QtWidgets.QMenu(self.menubar)
        self.menuMENU_2.setObjectName("menuMENU_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHOME = QtWidgets.QAction(MainWindow)
        self.actionHOME.setObjectName("actionHOME")
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        self.actionEXIT.setObjectName("actionEXIT")
        self.menuMENU.addAction(self.actionHOME)
        self.menuMENU.addAction(self.actionEXIT)
        self.menubar.addAction(self.menuMENU.menuAction())
        self.menubar.addAction(self.menuMENU_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CHECK DROWSINESS"))
        self.pushButton_2.setText(_translate("MainWindow", "RECOGNIZE DRIVER"))
        self.label.setText(_translate("MainWindow", "                            REVIEW AREA"))
        self.pushButton_3.setText(_translate("MainWindow", "Click To Speak"))
        self.label_2.setText(_translate("MainWindow", "   Your Review"))
        self.label_3.setText(_translate("MainWindow", "  FNAME"))
        self.label_4.setText(_translate("MainWindow", " LNAME"))
        self.label_5.setText(_translate("MainWindow", " USERNAME"))
        self.pushButton_4.setText(_translate("MainWindow", "SUBMIT"))
        self.menuMENU.setTitle(_translate("MainWindow", "OPTION"))
        self.menuMENU_2.setTitle(_translate("MainWindow", "MENU"))
        self.actionHOME.setText(_translate("MainWindow", "HOME"))
        self.actionEXIT.setText(_translate("MainWindow", "EXIT"))
        self.actionHOME.triggered.connect(self.home)
        self.actionEXIT.triggered.connect(self.end)
        self.menuMENU.triggered.connect(self.ShowMENU)
        self.pushButton.clicked.connect(self.SleepDetect)        
        self.pushButton_2.clicked.connect(self.FaceRecognize)
        self.pushButton_3.clicked.connect(self.SpeechToText)
        self.pushButton_4.clicked.connect(self.Submit)
        
        
    def home(self):
        self.frame.show()
   
    def end(self):
        sys.exit()  
   
    def ShowMENU(self):
        self.frame.show()
    
    def SleepDetect(self):

        def get_landmarks(im):
            rects = detector(im, 1)

            if len(rects) > 1:
                return "error"
            if len(rects) == 0:
                return "error"
            return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])


        def annotate_landmarks(im, landmarks):
            im = im.copy()
            for idx, point in enumerate(landmarks):
                pos = (point[0, 0], point[0, 1])
                cv2.putText(im, str(idx), pos,
                    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                    fontScale=0.4,
                    color=(0, 0, 255))
                cv2.circle(im, pos, 3, color=(0, 255, 255))
            return im

        def top_lip(landmarks):
            top_lip_pts = []
            for i in range(50,53):
                top_lip_pts.append(landmarks[i])
            for i in range(61,64):
                    top_lip_pts.append(landmarks[i])
            top_lip_all_pts = np.squeeze(np.asarray(top_lip_pts))
            top_lip_mean = np.mean(top_lip_pts, axis=0)
            return int(top_lip_mean[:,1])


        def bottom_lip(landmarks):
            bottom_lip_pts = []
            for i in range(65,68):
                bottom_lip_pts.append(landmarks[i])
            for i in range(56,59):
                bottom_lip_pts.append(landmarks[i])
            bottom_lip_all_pts = np.squeeze(np.asarray(bottom_lip_pts))
            bottom_lip_mean = np.mean(bottom_lip_pts, axis=0)
            return int(bottom_lip_mean[:,1])
        
        def mouth_open(image):
            landmarks = get_landmarks(image)
            
            if landmarks == "error":
                return image, 0
            
            image_with_landmarks = annotate_landmarks(image, landmarks)
            top_lip_center = top_lip(landmarks)
            bottom_lip_center = bottom_lip(landmarks)
            lip_distance = abs(top_lip_center - bottom_lip_center)
            return image_with_landmarks, lip_distance
        
            #cv2.imshow('Result', image_with_landmarks)
            #cv2.imwrite('image_with_landmarks.jpg',image_with_landmarks)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
        def sound_alarm(path):
        	# play an alarm sound
        	playsound.playsound(path)
        
        def eye_aspect_ratio(eye):
        	# compute the euclidean distances between the two sets of
        	# vertical eye landmarks (x, y)-coordinates
        	A = dist.euclidean(eye[1], eye[5])
        	B = dist.euclidean(eye[2], eye[4])
        
        	# compute the euclidean distance between the horizontal
        	# eye landmark (x, y)-coordinates
        	C = dist.euclidean(eye[0], eye[3])
        
        	# compute the eye aspect ratio
        	ear = (A + B) / (2.0 * C)
        
        	# return the eye aspect ratio
        	return ear
         
        # construct the argument parse and parse the arguments
        
        cap = cv2.VideoCapture(0)
        yawns = 0
        yawn_status = False 
         
        # define two constants, one for the eye aspect ratio to indicate
        # blink and then a second constant for the number of consecutive
        # frames the eye must be below the threshold for to set off the
        # alarm
        EYE_AR_THRESH = 0.3
        EYE_AR_CONSEC_FRAMES = 30
        
        # initialize the frame counter as well as a boolean used to
        # indicate if the alarm is going off
        COUNTER = 0
        ALARM_ON = False
        
        # initialize dlib's face detector (HOG-based) and then create
        # the facial landmark predictor
        print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        
        # grab the indexes of the facial landmarks for the left and
        # right eye, respectively
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        
        # start the video stream thread
        print("[INFO] starting video stream thread...")
        #vs = VideoStream(src=0).start()
        time.sleep(1.0)
        
        # loop over frames from the video stream
        while True:
            ret, frame = cap.read()
            frame = imutils.resize(frame, width=450)
            image_landmarks, lip_distance = mouth_open(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rects = detector(gray, 0)
            
            prev_yawn_status = yawn_status  
            
            if lip_distance > 15:
                yawn_status = True 
                
                cv2.putText(frame, "Subject is Yawning", (50,450), 
                            cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
                
        
                output_text = " Yawn Count: " + str(yawns + 1)
        
                cv2.putText(frame, output_text, (50,50),
                            cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
                
            else:
                yawn_status = False 
                 
            if prev_yawn_status == True and yawn_status == False:
                yawns += 1
                if yawns > 4:
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
        				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    t = Thread(target=sound_alarm,args = ("alarm.wav",))
                    t.deamon = True
                    t.start()
                    yawns = 0
                    
        
            #cv2.imshow('Live Landmarks', image_landmarks )
            cv2.imshow('Yawn Detection', frame )
            
            for rect in rects:
                
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
        
        		# extract the left and right eye coordinates, then use the
        		# coordinates to compute the eye aspect ratio for both eyes
                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
        
        		# average the eye aspect ratio together for both eyes
                ear = (leftEAR + rightEAR) / 2.0
        
        		# compute the convex hull for the left and right eye, then
        		# visualize each of the eyes
                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        		# check to see if the eye aspect ratio is below the blink
        		# threshold, and if so, increment the blink frame counter
                if ear < EYE_AR_THRESH:
                    COUNTER += 1
        
        			# if the eyes were closed for a sufficient number of
        			# then sound the alarm
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
        				# if the alarm is not on, turn it on
                        if not ALARM_ON:
                            ALARM_ON = True
        
        					# check to see if an alarm file was supplied,
        					# and if so, start a thread to have the alarm
        					# sound played in the background
                            if "alarm.wav" != "":
                                t = Thread(target=sound_alarm,args = ("alarm.wav",))
                                t.deamon = True
                                t.start()
        
        				# draw an alarm on the frame
                        cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
        					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        		# otherwise, the eye aspect ratio is not below the blink
        		# threshold, so reset the counter and alarm
                else:
                    COUNTER = 0
                    ALARM_ON = False
        
        		# draw the computed eye aspect ratio on the frame to help
        		# with debugging and setting the correct eye aspect ratio
        		# thresholds and frame counters
                cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
        			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
         
        	# show the frame
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
         
        	# if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows() 
    
    def FaceRecognize(self):
        
        print("[INFO] loading encodings...")
        data = pickle.loads(open("C:/Users/ShoryaSharma/Documents/IBM Project/face-recognition-opencv/encodings_project.pickle", "rb").read())
        
        # initialize the video stream and pointer to output video file, then
        # allow the camera sensor to warm up
        print("[INFO] starting video stream...")
        #vs = VideoStream(src=0).start()
        cap = cv2.VideoCapture(0)
        writer = None
        time.sleep(2.0)
        
        # loop over frames from the video file stream
        while True:
            ret, frame = cap.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = imutils.resize(frame, width=750)
            r = frame.shape[1] / float(rgb.shape[1])
            boxes = face_recognition.face_locations(rgb,
        		model="hog")
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []
            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"],
        			encoding)
                name = "Unknown"
                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)
                names.append(name)
                for ((top, right, bottom, left), name) in zip(boxes, names):
                    top = int(top * r)
                    right = int(right * r)
                    bottom = int(bottom * r)
                    cv2.rectangle(frame, (left, top), (right, bottom),
        			(0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
        			0.75, (0, 255, 0), 2)
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        
        cap.release()
        cv2.destroyAllWindows() 
        
    def SpeechToText(self):
        global r1
        r = sr.Recognizer()
        mic = sr.Microphone()
        
        with mic as source:
            print("start speaking...................................................")
            #self.textEdit.setText("start speaking")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            #print("Thanks")
            self.textEdit.setText("Thanks")
        r1 = r.recognize_google(audio)
        print(r1)        
        self.textEdit_2.setText(r1)
    
    def Submit(self): 
        response = natural_language_understanding.analyze(
            text=r1,features=Features(sentiment=SentimentOptions())).get_result()
        print(json.dumps(response, indent=2))
        response = response["sentiment"]["document"]["label"]
        print(response)
        text1 = self.textEdit_3.toPlainText()
        text2 = self.textEdit_4.toPlainText()
        text3 = self.textEdit_5.toPlainText()
        
        try:
            conn = ibm_db.connect(dsn, "", "")
            print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
        
        except:
            print ("Unable to connect: ", ibm_db.conn_errormsg() )
        
        insertQuery = "insert into REVIEW values (?, ?, ?, ?, ?)"
        params=(text3,text1,text2,r1,response)
        stmt = ibm_db.prepare(conn, insertQuery)
        ibm_db.execute(stmt,params)
        ibm_db.close(conn)
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


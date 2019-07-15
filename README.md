# Drowsiness-Detection-And-Face-recognition-With Spoken Reviews
The agenda of the Project is to build an app to detect detect drowsiness of the drivers of a cab , match faces of drivers in real time and get spoken reviews from passengers.


# TYPICAL SCENARIO

1.	When travelling via a cab, the passenger sits at the back seat and the rider is in front, the passenger has no idea whether the driver has taken a proper nap or not or whether the driver is over doing his shift without sleeping. Drowsy driving can cause serious accidents. In U.S alone there are more than 80,000 Crashes a year involving drowsy driving. The application can detect whether the driver is feeling drowsy or not. 
2.	Many a times I had the experience where the face of the driver is not matching the face on the profile of the driver. When questioned on the same the usual response is “This is an old picture”. So, what my application proposes to do is to match the face of the driver in real time with multiple images saved in the database over different point of time. 
3.	The user can also five their reviews by simply speaking and providing few details. The application will analyze the sentiments of the user and will store the review along the sentiment in the database for taking insights in the future. 

# TECHNOLOGIES USED

1.	OpenCV
2.	Dlib
3.	Watson Natural language understanding. 
4.	Ibm_db
5.	PyQt

# Explanation part:
1.	The problems we are dealing with here are drowsy driving, Fraud Identity and spoken reviews. 
2.	When travelling via a cab, the passenger sits at the back seat and the rider is in front, the passenger has no idea whether the driver has taken a proper nap or not or whether the driver is over doing his shift without sleeping. Drowsy driving can cause serious accidents. In U.S alone there are more than 80,000 Crashes a year involving drowsy driving. 
3.	Also, many a times I had the experience where the face of the driver is not matching the face on the profile of the driver. When questioned on the same the usual response is “This is an old picture., This is the case of fraud identity.
4.	Many apps do not allow to share your experience as a review what they ask you to di is rate the ride. 
5.	So, what this application does is that it detects whether the driver is feeling sleepy or not i.e. it can detect drowsiness. If the driver is feeling sleepy an alarm is set on automatically to wake up the driver. 
6.	The drowsiness is detected by yawn and whether the eyes are closed or not. If one the case is true, the alarm will be set on. The minimum yawns before the alarm is 5 and the minimum frames for detecting the sleep is 30 frames.
7.	The application is capable of recognizing Faces in real time. It matches the face in front of the camera with the faces stored in the database and displays the name on the screen.
8.	The users can also give their reviews by simply speaking and providing few details. 
9.	For making the project I used various techniques and libraries, these are OpenCV, Dlib, Watson NLU, IBM_DB2, PyQt framework, Google speech recognition, Deep metric Learning, Resnet-34.
10.	OpenCV stands for open source computer vision, OpenCV is a library mainly aimed at real-time computer vision.
11.	I used OpenCV for reading faces from camera, doing some modifications on the image read and then displaying or storing the resulted image. 
12.	Dlib is a toolkit for making real world machine learning and data analysis applications.  The dlib library, maintained by Davis King, contains our implementation of “deep metric learning” which is used to construct our face embeddings used for the actual recognition process. The pre-trained facial landmark detector inside the dlib library is used to estimate the location of 68 (x, y)-coordinates that map to facial structures on the face.
13.	Natural language understanding (NLU) is a branch of artificial intelligence (AI) that uses computer software to understand input made in the form of sentences in text or speech format. Watson natural language understanding is used to analyze text to extract metadata from content such as concepts, entities, keywords, categories, sentiment, emotion, relations, and semantic roles using natural language understanding. We have used Watson NLU for sentiment analysis only. 
14.	Qt Designer is the Qt tool for designing and building graphical user interfaces (GUIs) with Qt Widgets. You can compose and customize your windows or dialogs in a what-you-see-is-what-you-get (WYSIWYG) manner and test them using different styles and resolutions.
15.	IBM Db2 on Cloud is an SQL database. We can use Db2 on Cloud just as we would use any database software, but without the time and expense of hardware setup or software installation and maintenance.



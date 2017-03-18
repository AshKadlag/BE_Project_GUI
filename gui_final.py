#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui
import webbrowser
import urllib
'''
import cv2
import sys
from resnet50 import ResNet50
from keras.preprocessing import image
from imagenet_utils import preprocess_input, decode_predictions
import numpy as np
import cv2.cv as cv
import time
import cv2
exit = 0
model = ResNet50(weights='imagenet')
'''


def start_application():
	app1 = QtGui.QWidget()
	GUI1 = MainMenu()
	sys.exit(app1.exec_())

def label_image():
	app2 = QtGui.QWidget()
	GUI2 = LabelImage()
	sys.exit(app2.exec_())

def label_video():
	print("label video")

def extract_parameters():
	print("extract parameters")

def file_open():
	name = QtGui.QFileDialog.getOpenFileName()
	Image = QtGui.QImage()
	Image.load(name)
	Image.save("/home/root123456/Desktop/MachineLearning/ProjectCodes/GUIv1/sample.jpg","JPG",-1)
	app1 = QtGui.QWidget()
	GUI1 = LabelImageChildWindow()
	sys.exit(app1.exec_())

def camera_open():
	print("open camera")
	camera = cv2.VideoCapture(0)

	while True:
		return_value, image = camera.read()
		cv2.imshow('image', image)
		if cv2.waitKey(1) & 0xFF == ord ('q'):
			cv2.imwrite('sample.jpg',image)
			break
	camera.release()
	cv2.destroyAllWindows()

def chrome_open():
	print("web image")
	webbrowser.open('https://images.google.com/')

def url_child_open():
	app1 = QtGui.QWidget()
	GUI1 = LabelImageChildWindow()
	sys.exit(app1.exec_())

def drag_drop():
		print('drag drop')



class StartWindow(QtGui.QMainWindow):
	def __init__(self):
		super(StartWindow, self).__init__()

		startAction = QtGui.QAction("&Start",self)
		startAction.triggered.connect(start_application)

		closeAction = QtGui.QAction("&Exit",self)
		closeAction.triggered.connect(self.close_application)
		
		labelimage = QtGui.QAction("&Label Image",self)
		labelimage.triggered.connect(label_image)

		labelvideo = QtGui.QAction("&Label Image",self)
		labelvideo.triggered.connect(label_video)

		extractparameters = QtGui.QAction("&Label Image",self)
		extractparameters.triggered.connect(extract_parameters)

		mainMenu = self.menuBar()

		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(startAction)
		fileMenu.addAction(closeAction)

		optionsMenu = mainMenu.addMenu("&Options")
		optionsMenu.addAction(labelimage)
		optionsMenu.addAction(labelvideo)
		optionsMenu.addAction(extractparameters)

		pixmap = QtGui.QPixmap("background.jpg")
		lbl = QtGui.QLabel(self)
		lbl.setPixmap(pixmap)
		lbl.resize(lbl.minimumSizeHint())

		self.setGeometry(1, 1, 2000, 1800)
		self.setWindowTitle("Visual Recognition using CNN")
		self.show()

		QtCore.QTimer.singleShot(2000, start_application)

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Exit',
                                                "Do you want to exit?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass

class MainMenu(QtGui.QWidget):
	def __init__(self):
		super(MainMenu, self).__init__()
		
		self.createMenu()

		buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
		buttonBox.accepted.connect(start_application)
		buttonBox.rejected.connect(self.close_application)
		buttonBox.setStyleSheet("QPushButton { color: rgb(50,80,109);\
            font-size: 12pt;border: ;background-color: rgb(255, 255, 255);\
            border-style: outset;border-width: 2px;border-radius: 5px;\
            border-color: white;padding: 4px;}");
		
		btn1 = QtGui.QPushButton("Label a Image", self)
		btn1.clicked.connect(self.imageLabel)
		btn1.setIcon(QtGui.QIcon('camera2.png'))
		btn1.setIconSize(QtCore.QSize(130,130))
		btn1.setGeometry(QtCore.QRect(1030, 500, 161, 61))
		btn1.setFixedWidth(300)
		btn1.setFixedHeight(170)
		btn1.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 16pt;border: ;background-color: rgb(10,180,255);\
            border-style: outset;border-width: 2px;border-radius: 15px;\
            border-color: white;padding: 4px;} QPushButton: ");
		'''
		btn1.resize(250,150)
		btn1.move(300,200)
		'''

		btn2 = QtGui.QPushButton("Label a Video", self)
		btn2.clicked.connect(self.imageLabel)
		btn2.setIcon(QtGui.QIcon('video.png'))
		btn2.setIconSize(QtCore.QSize(130,130))
		btn2.setGeometry(QtCore.QRect(1030, 500, 161, 61))
		btn2.setFixedWidth(300)
		btn2.setFixedHeight(170)
		btn2.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 16pt;border: ;background-color: rgb(10,180,255);\
            border-style: outset;border-width: 2px;border-radius: 15px;\
            border-color: white;padding: 4px;}");
		'''
		btn2.resize(250,150)
		btn2.move(1000,200)
		'''

		btn3 = QtGui.QPushButton("Extract\nParameters", self)
		btn3.clicked.connect(self.imageLabel)
		btn3.setIcon(QtGui.QIcon('airplane-shape.png'))
		btn3.setIconSize(QtCore.QSize(130,130))
		btn3.setGeometry(QtCore.QRect(1030, 500, 161, 61))
		btn3.setFixedWidth(300)
		btn3.setFixedHeight(170)
		btn3.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 16pt;border: ;background-color: rgb(10,180,255);\
            border-style: outset;border-width: 2px;border-radius: 15px;\
            border-color: white;padding: 4px;}");
		'''
		btn3.resize(250,150)
		btn3.move(200,500)
		'''

		btn4 = QtGui.QPushButton("Label1", self)
		btn4.clicked.connect(self.imageLabel)
		btn4.setIcon(QtGui.QIcon('search.png'))
		btn4.setIconSize(QtCore.QSize(130,130))
		btn4.setGeometry(QtCore.QRect(1030, 500, 161, 61))
		btn4.setFixedWidth(300)
		btn4.setFixedHeight(170)
		btn4.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 16pt;border: ;background-color: rgb(10,180,255);\
            border-style: outset;border-width: 2px;border-radius: 15px;\
            border-color: white;padding: 4px;}");
		'''
		btn4.resize(250,150)
		btn4.move(600,500)
		'''

		btn5 = QtGui.QPushButton("Label2", self)
		btn5.clicked.connect(self.imageLabel)
		btn5.setIcon(QtGui.QIcon('smartphone.png'))
		btn5.setIconSize(QtCore.QSize(130,130))
		btn5.setGeometry(QtCore.QRect(1030, 500, 161, 61))
		btn5.setFixedWidth(300)
		btn5.setFixedHeight(170)
		btn5.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 16pt;border: ;background-color: rgb(10,180,255);\
            border-style: outset;border-width: 2px;border-radius: 15px;\
            border-color: white;padding: 4px;}");
		'''
		btn5.resize(250,150)
		btn5.move(1100,500)
		'''

		Hlayout1 = QtGui.QHBoxLayout()
		Hlayout1.addWidget(btn1)
		Hlayout1.addWidget(btn2)

		Hlayout2 = QtGui.QHBoxLayout()
		Hlayout2.addWidget(btn3)
		Hlayout2.addWidget(btn4)
		Hlayout2.addWidget(btn5)

		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addLayout(Hlayout1)
		mainLayout.addLayout(Hlayout2)
		mainLayout.addWidget(buttonBox)
		mainLayout.setMenuBar(self.menuBar)
		
		self.setLayout(mainLayout)
		
		#self.setStyleSheet("background-color: rgb(10,10,10);")
		self.setStyleSheet("background-image: url('background10.jpg');")
		#btn1.setStyleSheet(" { background-color: rgb(58,83,155); }")
		
		p = QtGui.QPalette()
		brush = QtGui.QBrush(QtCore.Qt.white,QtGui.QPixmap('background2.jpg'))
		p.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)
		p.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)
		p.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)
		self.setPalette(p)

		self.setGeometry(1, 1, 2000, 1800)
		self.setWindowTitle("Visual Recognition using CNN")
		self.show()

	def createMenu(self):
		self.menuBar = QtGui.QMenuBar()
		
		self.fileMenu = QtGui.QMenu("&File", self)

		self.startAction = self.fileMenu.addAction("&Start")
		self.startAction.triggered.connect(start_application)
		self.closeAction = self.fileMenu.addAction("&Exit")
		self.closeAction.triggered.connect(self.close_application)
		
		self.optionsMenu = QtGui.QMenu("&Options", self)
		
		self.labelimage = self.optionsMenu.addAction("&Label Image")
		self.labelimage.triggered.connect(label_image)
		self.labelvideo = self.optionsMenu.addAction("&Label Video")
		self.labelvideo.triggered.connect(label_video)
		self.extractparameters = self.optionsMenu.addAction("&Extract Parameters")
		self.extractparameters.triggered.connect(extract_parameters)

		self.menuBar.addMenu(self.fileMenu)
		self.menuBar.addMenu(self.optionsMenu)

	def imageLabel(self):
		app3 = QtGui.QMainWindow()
		GUI3 = LabelImage()
		sys.exit(app3.exec_())

	def createParameterBox(self):
		self.parameterBox = QtGui.QGroupBox()
		layout = QtGui.QHBoxLayout()

		label1 = QtGui.QLabel()
		label2 = QtGui.QLabel()
		label3 = QtGui.QLabel()
		label4 = QtGui.QLabel()

		label1.setText("Error Rate")
		label2.setText("Momemtum")
		label3.setText("Mini Batch Size")
		label4.setText("Training Iterations")
		
		layout.addWidget(label1)
		layout.addWidget(label2)
		layout.addWidget(label3)
		layout.addWidget(label4)

		self.parameterBox.setLayout(layout)

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Exit',
                                                "Do you want to exit?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass


class LabelImage(QtGui.QWidget):
	def __init__(self):
		super(LabelImage, self).__init__()
		
		self.createMenu()
		self.createHorizontalGroupBox()

		buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
		buttonBox.accepted.connect(start_application)
		buttonBox.rejected.connect(self.close_application)

		mainLayout = QtGui.QVBoxLayout()
		mainLayout.setMenuBar(self.menuBar)
		mainLayout.addWidget(self.horizontalGroupBox)

		mainLayout.addWidget(buttonBox)
		
		self.setLayout(mainLayout)
		
		p = QtGui.QPalette()
		brush = QtGui.QBrush(QtCore.Qt.white,QtGui.QPixmap('background22.jpg'))
		p.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)
		p.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)
		p.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)
		self.setPalette(p)

		
		#self.setStyleSheet("background-image: url('background10.jpg');")
		#self.setStyleSheet("background-color: rgb(255,255,255);")
		self.setGeometry(1, 1, 2000,1800)
		self.move(500,200)
		self.setWindowTitle("Visual Recognition using CNN")
		self.show()

	def createMenu(self):
		self.menuBar = QtGui.QMenuBar()
		
		self.fileMenu = QtGui.QMenu("&File", self)
		
		self.startAction = self.fileMenu.addAction("&Start")
		self.startAction.triggered.connect(start_application)
		self.closeAction = self.fileMenu.addAction("&Exit")
		self.closeAction.triggered.connect(self.close_application)
		
		self.optionsMenu = QtGui.QMenu("&Options", self)
		
		self.labelimage = self.optionsMenu.addAction("&Label Image")
		self.labelimage.triggered.connect(label_image)
		self.labelvideo = self.optionsMenu.addAction("&Label Video")
		self.labelvideo.triggered.connect(label_video)
		self.extractparameters = self.optionsMenu.addAction("&Extract Parameters")
		self.extractparameters.triggered.connect(extract_parameters)

		self.menuBar.addMenu(self.fileMenu)
		self.menuBar.addMenu(self.optionsMenu)

	def createHorizontalGroupBox(self):
		self.horizontalGroupBox = QtGui.QGroupBox()
		layout = QtGui.QHBoxLayout()
		
		title = QtGui.QLabel("Select Image Source:")
		title.setStyleSheet("QLabel {color: rgb(0,0,0); font-size: 18pt;}")
		title.setFixedHeight(50)
		
		btn1 = QtGui.QPushButton("Browse", self)
		btn1.clicked.connect(file_open)
		btn1.setFixedWidth(300)
		btn1.setFixedHeight(100)
		btn1.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 18pt;border: ;background-image: url('background1.jpg');\
            border-style: outset;border-width: 2px;border-radius: 10px;\
            border-color: white;padding: 10px;}");
		btn1.resize(btn1.minimumSizeHint())
		btn1.move(4,10)
		
		btn2 = QtGui.QPushButton("Camera", self)
		btn2.clicked.connect(camera_open)
		btn2.setFixedWidth(300)
		btn2.setFixedHeight(100)
		btn2.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 18pt;border: ;background-image: url('background1.jpg');\
            border-style: outset;border-width: 2px;border-radius: 10px;\
            border-color: white;padding: 10px;}");
		btn2.resize(btn2.minimumSizeHint())
		btn2.move(4,50)

		btn3 = QtGui.QPushButton("Search", self)
		btn3.clicked.connect(chrome_open)
		btn3.setFixedWidth(300)
		btn3.setFixedHeight(100)
		btn3.setStyleSheet("QPushButton { color: rgb(0,0,0);\
            font-size: 18pt;border: ;background-image: url('background1.jpg');\
            border-style: outset;border-width: 2px;border-radius: 10px;\
            border-color: white;padding: 10px;}");
		btn3.resize(btn3.minimumSizeHint())
		btn3.move(4,100)

		label = QtGui.QLabel("Enter Image URL: ")
		label.setStyleSheet("QLabel {color: rgb(0,0,0); font-size: 18pt;background-image: url('background1.jpg');\
            border-style: outset;border-width: 2px;border-radius: 10px;\
            border-color: white;padding: 10px;}")
		self.url = QtGui.QLineEdit()

		name = self.url.text()
		print (name)
		btnok = QtGui.QPushButton("Ok",self)
		btnok.clicked.connect(self.url_image_save)

		boxurl = QtGui.QHBoxLayout()
		boxurl.addWidget(label)
		boxurl.addWidget(self.url)
		boxurl.addWidget(btnok)
		
		'''
		btn4 = QtGui.QPushButton("Drag and Drop", self)
		btn4.clicked.connect(drag_drop)
		btn4.setStyleSheet("QPushButton { color: rgb(255, 255, 255);\
            font-size: 16pt;border: ;background-color: rgb(50,80,109);\
            border-style: outset;border-width: 2px;border-radius: 10px;\
            border-color: white;padding: 10px;}");
		btn4.resize(btn4.minimumSizeHint())
		btn4.move(4,150)
		'''

		vbox1 = QtGui.QVBoxLayout()
		vbox1.addWidget(title,1)
		vbox1.addWidget(btn1,2)
		vbox1.addWidget(btn2,2)
		vbox1.addWidget(btn3,2)
		vbox1.addLayout(boxurl,1)
		#vbox1.addWidget(btn4)

		layout.addLayout(vbox1)

		self.horizontalGroupBox.setLayout(layout)

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Exit',
                                                "Do you want to exit?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass

	def url_image_save(self):
		url_of_image = self.url.text()
		print url_of_image
		url_of_image = str(url_of_image)
		urllib.urlretrieve(url_of_image, "sample.jpg")
		url_child_open()


class LabelImageChildWindow(QtGui.QWidget):
	def __init__(self):
		super(LabelImageChildWindow, self).__init__()

		self.createMenu()
		self.createParameterBox()
		self.label_image()

		buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
		buttonBox.accepted.connect(label_image)
		buttonBox.rejected.connect(self.close_application)

		#self.horizontalGroupBox = QtGui.QGroupBox()
		#self.layout = QtGui.QHBoxLayout()
		#self.horizontalGroupBox.setLayout(self.layout)
		mainLayout = QtGui.QVBoxLayout()
		mainLayout.setMenuBar(self.menuBar)
		#mainLayout.addWidget(self.horizontalGroupBox)
		mainLayout.addWidget(self.labelimage,5)
		mainLayout.addWidget(self.parameterBox,1)
		mainLayout.addWidget(buttonBox,1)
		self.setLayout(mainLayout)
		

		#self.setStyleSheet("background-image: url('background10.jpg');")
		#btn1.setStyleSheet(" { background-color: rgb(58,83,155); }")
		
		p = QtGui.QPalette()
		brush = QtGui.QBrush(QtCore.Qt.white,QtGui.QPixmap('background19.jpg'))
		p.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)
		p.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)
		p.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)
		self.setPalette(p)
		
		#self.setStyleSheet("background-color: rgb(255,255,255);")
		self.setGeometry(1, 1, 2000, 1800)
		#self.move(300,10)
		self.setWindowTitle("Visual Recognition using CNN")
		self.show()

	def label_image(self):    
		self.labelimage = QtGui.QGroupBox()
		hlayout = QtGui.QHBoxLayout()
		pixmap = QtGui.QPixmap("sample.jpg")
		newPix = pixmap.scaled(300, 700, QtCore.Qt.KeepAspectRatio)
		#pixmap_resized = pixmap.scaled(720, 405, QtCore.Qt.KeepAspectRatio)
		lbl = QtGui.QLabel(self)
		lbl.setPixmap(newPix)
		lbl.setAlignment(QtCore.Qt.AlignCenter)
		#lbl.setStyleSheet("QLabel {background-color: red;}")
		#lbl.resize(700, 900)
		#lbl.move(0,0)
		#i = QtGui.QWidget(lbl)
		#lbl.setFixedSize(1250, 900)

		'''
		img = image.load_img('sample', target_size=(224, 224))

		x = image.img_to_array(img)	
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
		preds = model.predict(x)
		result  = decode_predictions(preds)
		'''

		#for i in range(0,len(result[0])):
		#	print result[0][i][1]
			#print len(result)
		#print result
		'''
		label = np.zeros(5)
		vbox2 = QtGui.QVBoxLayout()
		for i in range(len(label)):
			label[i]  = QtGui.QLabel()
			label[i].setText(result[0][i][1])
        	label[i].setAlignment(QtCore.Qt.AlignCenter)
        	label[i].setStyleSheet("QLabel { color: white;\
            	font-size: 16pt; background-color: rgb(77, 194, 71);\
            	border-style: outset;border-radius: 7px;border-color: white;}");
        	label[i].setFixedSize(200,60)
        	vbox2.addWidget(label[i])
        
		'''
		label1 = QtGui.QLabel()
		label2 = QtGui.QLabel()
		label3 = QtGui.QLabel()
		label4 = QtGui.QLabel()
		label5 = QtGui.QLabel()

		label1.setText("1")
		#label1.setText(result[0][0][1])
		label1.setAlignment(QtCore.Qt.AlignCenter)
		label1.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 7px;border-color: white;}")

		label2.setText("2")
		#label2.setText(result[0][0][1])
		label2.setAlignment(QtCore.Qt.AlignCenter)
		label2.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 7px;border-color: white;}")

		label3.setText("3")
		#label3.setText(result[0][0][1])
		label3.setAlignment(QtCore.Qt.AlignCenter)
		label3.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 7px;border-color: white;}")

		label4.setText("4")
		#label4.setText(result[0][0][1])
		label4.setAlignment(QtCore.Qt.AlignCenter)
		label4.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 7px;border-color: white;}")

		label5.setText("5")
		#label5.setText(result[0][0][1])
		label5.setAlignment(QtCore.Qt.AlignCenter)
		label5.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 7px;border-color: white;}")

		label1.setFixedSize(200,60)
		label2.setFixedSize(200,60)
		label3.setFixedSize(200,60)
		label4.setFixedSize(200,60)
		label5.setFixedSize(200,60)

		vbox2 = QtGui.QVBoxLayout()
		vbox2.addWidget(label1)
		vbox2.addWidget(label2)
		vbox2.addWidget(label3)
		vbox2.addWidget(label4)
		vbox2.addWidget(label5)

		hlayout.addWidget(lbl)
		hlayout.addLayout(vbox2)
		self.labelimage.setLayout(hlayout)
	
	def createMenu(self):
		self.menuBar = QtGui.QMenuBar()

		self.fileMenu = QtGui.QMenu("&File", self)

		self.startAction = self.fileMenu.addAction("&Start")
		self.startAction.triggered.connect(start_application)
		self.closeAction = self.fileMenu.addAction("&Exit")
		self.closeAction.triggered.connect(self.close_application)

		self.optionsMenu = QtGui.QMenu("&Options", self)

		self.labelimage = self.optionsMenu.addAction("&Label Image")
		self.labelimage.triggered.connect(label_image)
		self.labelvideo = self.optionsMenu.addAction("&Label Video")
		self.labelvideo.triggered.connect(label_video)
		self.extractparameters = self.optionsMenu.addAction("&Extract Parameters")
		self.extractparameters.triggered.connect(extract_parameters)

		self.menuBar.addMenu(self.fileMenu)
		self.menuBar.addMenu(self.optionsMenu)

	def createParameterBox(self):
		self.parameterBox = QtGui.QGroupBox()
		layout1 = QtGui.QHBoxLayout()

		label1 = QtGui.QLabel()
		label2 = QtGui.QLabel()
		label3 = QtGui.QLabel()
		label4 = QtGui.QLabel()

		label1.setText("Error Rate")
		label1.setAlignment(QtCore.Qt.AlignCenter)
		label1.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");
		
		label2.setText("Momemtum")
		label2.setAlignment(QtCore.Qt.AlignCenter)
		label2.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");
		
		label3.setText("Mini Batch Size")
		label3.setAlignment(QtCore.Qt.AlignCenter)
		label3.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");
		
		label4.setText("Training Iterations")
		label4.setAlignment(QtCore.Qt.AlignCenter)
		label4.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");

		layout1.addWidget(label1)
		layout1.addWidget(label2)
		layout1.addWidget(label3)
		layout1.addWidget(label4)

		layout2 = QtGui.QHBoxLayout()

		label11 = QtGui.QLabel()
		label22 = QtGui.QLabel()
		label33 = QtGui.QLabel()
		label44 = QtGui.QLabel()

		label11.setText("Error Rate")
		label11.setAlignment(QtCore.Qt.AlignCenter)
		label11.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");
		
		label22.setText("Momemtum")
		label22.setAlignment(QtCore.Qt.AlignCenter)
		label22.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");
		
		label33.setText("Mini Batch Size")
		label33.setAlignment(QtCore.Qt.AlignCenter)
		label33.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");
		
		label44.setText("Training Iterations")
		label44.setAlignment(QtCore.Qt.AlignCenter)
		label44.setStyleSheet("QLabel { color: rgb(77, 194, 71);\
            font-size: 16pt; background-color: white;\
            border-style: outset;border-radius: 5px;border-color: white;}");

		layout2.addWidget(label11)
		layout2.addWidget(label22)
		layout2.addWidget(label33)
		layout2.addWidget(label44)

		layout = QtGui.QVBoxLayout()
		layout.addLayout(layout1)
		layout.addLayout(layout2)

		self.parameterBox.setLayout(layout)

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Exit',
                                                "Do you want to exit?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass



def run():
	app = QtGui.QApplication(sys.argv)
	GUI = StartWindow()
	sys.exit(app.exec_())


run()

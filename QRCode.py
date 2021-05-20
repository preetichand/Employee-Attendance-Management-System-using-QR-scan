
import pyzbar.pyzbar as pyzbar
import cv2
import numpy
import qrcode
import datetime 

class QRCode:
	def generate(self):
		current_time = datetime.datetime.now()
		id=str(current_time.year)+str(current_time.month)+str(current_time.day)
		id=id+str(current_time.hour)+str(current_time.minute)+str(current_time.second)
		img = qrcode.make(id)
		img.save(id+".jpg")
		return id;


	def scan(self):
		i=0
		cap=cv2.VideoCapture(0)
		while i<1:
			_,frame=cap.read()
			decode=pyzbar.decode(frame)
			for obj in decode:
				s.append(obj.data.decode())
				i=i+1
			cv2.imshow("QRCode",frame)
			cv2.waitKey(5)
			cv2.destroyAllWindows

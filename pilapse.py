from time import sleep
import picamera

WAIT_TIME = 10
num = 0

with picamera.PiCamera() as camera:
	camera.resolution = (1920, 1080)
	for filename in camera.capture_continuous('/media/pi/PICSTICK/img{counter:06d}.jpg'):
		num+=1
		print(num)
		sleep(WAIT_TIME)

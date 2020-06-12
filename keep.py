import pyautogui as pa
import time

resolution=pa.size()
x=resolution[0]
y=resolution[1]


while True:
	pa.moveTo(x/2,y/2) 	#Change the location to move your mouse here
	time.sleep(5)  #Change sleep time here 
	pa.moveTo(x/2+25,y/2+25) #Change the location to move your mouse here
	time.sleep(5) #Change sleep time here


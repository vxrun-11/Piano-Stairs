import pygame
from pygame import mixer
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7, GPIO.OUT)
'''GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)'''
pygame.mixer.init()
while True:
	if GPIO.input(8)==1:
		mixer.Sound(f'notes//C3.wav').play(0,1000)
		GPIO.output(7,True)
	else:
        GPIO.output(7,False)
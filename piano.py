import pygame
from pygame import mixer
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(7,GPIO.OUT)
pygame.mixer.init()
while True:
	if GPIO.input(8)==1:
		mixer.Sound(f'notes//C3.wav').play(0,1000)
		GPIO.output(7,True)
	if GPIO.input(10)==1:
		mixer.Sound(f'notes//D3.wav').play(0,1000)
		GPIO.output(7,True)
	if GPIO.input(11)==1:
		mixer.Sound(f'notes//E3.wav').play(0,1000)
		GPIO.output(7,True)
	if GPIO.input(12)==1:
		mixer.Sound(f'notes//F3.wav').play(0,1000)
		GPIO.output(7,True)
	if GPIO.input(13)==1:
		mixer.Sound(f'notes//G3.wav').play(0,1000)
		GPIO.output(7,True)
	if GPIO.input(15)==1:
		mixer.Sound(f'notes//A3.wav').play(0,1000)
		GPIO.output(7,True)
	if GPIO.input(16)==1:
		mixer.Sound(f'notes//B3.wav').play(0,1000)
		GPIO.output(7,True)
	if GPIO.input(18)==1:
		mixer.Sound(f'notes//C4.wav').play(0,1000)
		GPIO.output(7,True)

	GPIO.output(7,False)
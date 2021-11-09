import pygame 
import time
#import matplotlib.pyplot as plt
#import imageio as io

print("Name:")
name = input()

pygame.mixer.init()
track = pygame.mixer.music.load(name+'.wav')

pygame.mixer.music.play()
time.sleep(3)

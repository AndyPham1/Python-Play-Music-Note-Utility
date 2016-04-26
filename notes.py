import pygame
import csv
import time
import random
import os
import site

FADEOUT_TIME = 500
TIME_BETWEEN_NOTES = 0.5
PATH_DEFAULT = os.path.join(site.getsitepackages()[1],"./notes/config.csv")
pygame.mixer.init()

#READ CONF FILE AND MAP SOUNDFILE AND SOUND, INPUT IS CONFIG FILE LOCATION
class Notes():
    def __init__(self, configurationMap=PATH_DEFAULT):
        self.key2sound = {}
        self.key2file = {}
        self.key = [] # possible mapping without using numbers
        self.keyNum = 0;
        config = csv.reader(open(configurationMap, 'r'), delimiter=',')
        for key,soundfile in config:
            key,soundfile = key.strip(' '),soundfile.strip(' ')
            if key is not '#':
                self.key.append(os.path.splitext(key)[0])
                self.key2file[self.keyNum] = soundfile
                self.key2sound[self.keyNum] = pygame.mixer.Sound(soundfile)
                self.keyNum+=1

#FUNCTION THAT PLAYS NOTES AND FADES IT OUT
    def playNote(self,number=0):
        self.key2sound[number].play(0)
        time.sleep(0.55)
        self.key2sound[number].fadeout(FADEOUT_TIME)

#FUNCTION THAT PLAYS N RANDOM NOTES
    def playRand(self,num=3):
       for x in range(num):
           rKey =  random.randint(1,self.keyNum-1)
           self.playNote(rKey)

#FUNCTION THAT PLAYS NOTES BASE ON STRING
    def playNotes(self,string):
        notes = string.split()
        print(notes)
        for note in notes:
            self.playNote(int(note))
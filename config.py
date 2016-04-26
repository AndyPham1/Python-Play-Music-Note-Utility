from glob import glob
import os
import csv

#Make config files. Put note collection to the soundfont folder 
#script it to make config file, set up each wav file as musical notes
#for the Note.py script. Call Note(config.csv) to use note

                
#input directory with sound font folder or
#change directory with folder with sounfont then run getConfig
def getConfig(directory='.'):
    files_list = glob(os.path.join(directory,'*.wav'))
    file_path = os.path.abspath(os.path.join(directory,'./soundfonts'))
    with open('config.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for file in os.listdir(file_path):
            if file.endswith(".wav"):
                abs_f_path = os.path.join(file_path,file)
                writer.writerow([file,abs_f_path])
        

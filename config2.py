from glob import glob
import os
import csv

#Make config files. Put note collection to the soundfont folder 
#script it to make config file, set up each wav file as musical notes
#for the Note.py script. Call Note(config.csv) to use note

files_list = glob('./soundfonts/*.wav')
file_path = os.path.abspath('./soundfonts')
with open('config.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for file in os.listdir("./soundfonts"):
        if file.endswith(".wav"):
            abs_f_path = os.path.join(file_path,file)
            writer.writerow([file,abs_f_path])
        

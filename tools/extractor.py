#!/usr/bin/env python3

import os
import subprocess

def process ():

    for filelist in os.walk(".") :
        file = filelist [2] 
        for file in filelist[2]:
            if (os.path.isfile(file)):
                cmd = "/opt/homebrew/bin/tesseract -l script/Devanagari " + \
                       file + " " + file+".txt"
                
                print ("Running : ",cmd)
                subprocess.run(cmd, shell=True)

 

if __name__ == "__main__":
    process()

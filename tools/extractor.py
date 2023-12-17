#!/usr/bin/env python3

import os
import subprocess

def process ():

    for filelist in os.walk(".") :
        file = filelist [2] 
        for file in filelist[2]:
            if (os.path.isfile(file)):
                #cmd = "/opt/homebrew/bin/tesseract -l script/Devanagari " + \
                if  file.endswith(".png") or file.endswith(".jpeg"):
                    # name of the file without extension 
                    cmd = "/opt/homebrew/bin/tesseract -l script/Kannada " + \
                           file + " " + file

                    print ("Running : ",cmd)
                    subprocess.run(cmd, shell=True)
            else:
                print ("Ignoring : ", file)
 

if __name__ == "__main__":
    process()

#
#
# from indic_transliteration import sanscript
# from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

# data = "श्रीमत्मध्वाचार्यभगवत्पादाचर्य"
# print(transliterate(data, sanscript.DEVANAGARI, sanscript.IAST))
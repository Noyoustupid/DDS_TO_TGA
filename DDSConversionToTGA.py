from PIL import Image
import os, subprocess, platform

#ogDir is starting directory, newDir is where the new files will be saved to
ogDir = 'C:\\users\\artur\\Desktop\\Abandoned Shack\\Textures'
newDir = 'C:\\users\\artur\\Desktop\\Abandoned Shack\\New Textures'

#loops through each directory, sub directory and file
for dirpath, dirnames, filenames in os.walk(ogDir):

    if not filenames: #if specific subdirectory has no files do nothing, if it has files then...
        ()
    else:
        for item in filenames:      #for each file name in the filenames (list, set?? whatever the name is) 
            if '.dds' in item:      # if the file has extension .dds then print the file directory combined with the file name
                newPath = dirpath.replace(ogDir,newDir)                     #takes current file directory and replaces the the parts that are original for new
                os.makedirs(newPath, exist_ok=True)                         #creates the new directory in the taget location     
                file = ''.join([dirpath,'\\',item])                         #joins the file name to the directory
                currentImage = Image.open(file)                             #opens the image
                newFile = file.replace(".dds",".tga").replace(ogDir,newDir) #changes the filetype and changes the the original image directory to the new one
                currentImage.save(newFile)                                  #saves the image in the new directory
               
print('Done')

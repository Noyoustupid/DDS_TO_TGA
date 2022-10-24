import os, subprocess, platform
from pynput.keyboard import Key, Controller
import time

#set the keyboard as the controller
keyboard = Controller()

#loops through each directory, sub directory and file
for dirpath, dirnames, filenames in os.walk('C:\\users\\artur\\Desktop\\Abandoned Shack\\Textures'):

    if not filenames: #if specific subdirectory has no files do nothing, if it has files then...
        ()
    else:
        for item in filenames:      #for each file name in the filenames (list, set?? whatever the name is) 
            if '.dds' in item:      # if the file has extension .dds then print the file directory combined with the file name
                filepath = ''.join([dirpath,'\\',item])
                                
                #open specified file with windows default application
                os.startfile(filepath)
                #wait for the window to open
                time.sleep(2.5)

                #send "save as" command to the window
                with keyboard.pressed(Key.shift):
                    with keyboard.pressed(Key.ctrl):
                        keyboard.press('s')
                        keyboard.release('s')

                # wait for the "save as" window to open
                time.sleep(1.5)
                #select TGA file format by going to file format selection window with TAB and pressing "t" twice
                keyboard.press(Key.tab)
                time.sleep(.75)
                keyboard.press('t')
                keyboard.release('t')
                time.sleep(.2)
                keyboard.press('t')
                keyboard.release('t')

                #press enter to save
                keyboard.press(Key.enter)
                time.sleep(.3)
                keyboard.press(Key.enter)

                # short delay for stability and close   
                time.sleep(3)
                with keyboard.pressed(Key.alt):
                    keyboard.press(Key.f4)

                time.sleep(.2)    
                os.remove(filepath)     #remove the old texture file

                
            
    

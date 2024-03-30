from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth 
import os
from capture import * 

# we have result from capture

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#opencv_frame_x.png

path = fr'/home/tanmay/Documents/code/ML/notesorganizer/buffer/opencv_frame_{result}.png'

os.system("xdg-open path")

for x in os.listdir(path):
    f=drive.CreateFile({'title':x})
    f.SetContentFile(os.path.join(path,x))
    f.Upload()


f=None

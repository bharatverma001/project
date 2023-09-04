import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2 
    videoCaptureObject = cv2.VideoCapture(0)
    result = True 
    while (result):
      
      # read the frames while the camera is on
     ret,frame = videoCaptureObject.read() 
     img_name = "img"+str(number)+".png" 
     cv2.imwrite(img_name, frame)
     start_time = time.time 
     result = False 
    return img_name 
    print("snapshot taken")   
    videoCaptureObject.release() 
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = "sl.BlDoe5DWHGQJcPJw4kruMG2ycwr9-miRyDlagkXN9FY4tfhj4D-6_5S8oX9jWQCbFvpzTekFEzWQLfkBGuOsGMjjSpiEbWtaKjLtDBGw8jusJDTuElij-hhPIXTzGCHpeUeCCOPQsnoc"
    take_snapshot()
    file=img_name
    file_from = img_name
    file_to = "/testfolder/"+file
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
     dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True): 
     if((time.time()-start_time)>=3):
        name=take_snapshot()
        upload_file(name)
main()
       
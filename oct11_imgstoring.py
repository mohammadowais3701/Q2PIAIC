import os
import PIL as pil
import numpy as np
def imageToNP(imageName):
    try:
        npa=pil.Image(imageName)
        return npa
    except(Exception):
        print("error")

def main():
   if file exist in path:
       img_array=np.load("file")
   else:
   path,dirs,files=next(os.walk("robots"))
   file_count=len(files)
   image_array=np.zeros([file_count,200,200,3])

   for files in next(os.walk("robots")):
      idx=0
      for file in files:
          img_array=(idx,imageToNP(file))
          idx=idx+1

if __name__=='__main__':
    main()
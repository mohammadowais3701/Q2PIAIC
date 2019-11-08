import numpy as np
import os
import matplotlib.pylab as plt
from PIL import Image
imgs=np.ones([5,512,512,3])
rootDir='robots'
for dirName,subDirName,fileList in os.walk(rootDir):
    print("Found Directory: %s" %dirName)
    for fname in fileList:
        imggs=Image.open("robots/"+fname)
        imgs = imggs.resize((300, 300))
        imggs.show()
print(imggs)
for i in range(0 ,5):
    plt.figure()
   # plt.imshow(imgs[4,:300,:300,3])
    #plt.show()





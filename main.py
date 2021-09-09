from PIL import Image
import os
from os import walk

def getImageCount():
    list = os.listdir('input')
    number_files = len(list)
    return number_files


def getFileList():
    list_files = []
    for (dirpath, dirnames, filenames) in walk('input'):
        list_files.extend(filenames)
        break
    return list_files

def convertToPdf():
    fileList = []
    count = 1
    for file in getFileList():
        if count != 1:
            image = Image.open('input/'+ file)
            im = image.convert('RGB')
            fileList.append(im)
        count += 1
        
    image = Image.open('input/'+ getFileList()[0])
    im = image.convert('RGB')
    im.save('output/output.pdf',save_all=True, append_images=fileList)

print('Tüm resim dosyalarınızı input klasoru icerisine koyunuz!')
input('Devam etmek icin ENTER tusuna basınız!')
try:
    convertToPdf()
    print('Donusturme islemi tamamlandı.')
except Exception as e:
    print(e)

            


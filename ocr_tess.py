import pytesseract
from PIL import Image
import cv2
import os
from pdf2image import convert_from_path




"""List of parameters"""

kidney=("Cretin level","Protein :=")
stroke=("BP (diastolic) :=","BP (systolic) :=","Pulse Rate:-")
liver=("Bilirubin Total","Bilirubin Direct","Bilirubin Indirect")


disease=input("Enter The disease whose report you are uploading:-")




def pdfocr(file,disease):
    string=""
    filexp=file.split(".")
    nm=filexp[0]
    i=1
    pages = convert_from_path(file, 500)
    for page in pages:
        name=nm+str(i)+'.jpg'
        page.save(name, 'JPEG')
        i=i+1

    fileimg = nm+str(1)+'.jpg'
    print(fileimg)
    img=cv2.imread(fileimg)

    text=pytesseract.image_to_string(img)
    print(text)

    if disease=="Kidney" or disease=='kidney':
        for i in kidney:
            #print(i)
            spl_word=i
            res=text.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            data.append(string)

    elif disease=="Stroke" or disease=="stroke":
        for i in stroke:
            #print(i)
            spl_word=i
            res=text.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            data.append(string)
    elif disease=="Liver" or disease=="liver":
        for i in liver:
            #print(i)
            spl_word=i
            res=text.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            data.append(string)

    return data


def imageocr(file,disease):
    print("Image OCR")


# In[24]:


#Upload the file
file=input("Enter the file name= ")

expand=file.split(".")

data=[]

if expand[0]=="p":
    data=pdfocr(file,disease)

else:
    data=imageocr(file,disease)

print(data)

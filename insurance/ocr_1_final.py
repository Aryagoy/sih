#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#OCR 4 (FINAL)


"""List of parameters includes the parameters the OCR will check for in the file add more diseases
according to the database created"""

"""This automatically detects if the file is a pdf or an image. PDF is handled by pdfocr() and image by imageocr()"""


# In[7]:


"""REQUIRED LIBRARY FILES"""                 """TESSERACT"""
import pytesseract
from PIL import Image
import cv2
import os
import json
import numpy as np
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
import re
import urllib.request
import requests


# In[22]:


"""List of parameters"""

vitals=("(MCV)","Hemoglobin","Cholestrol","Pulse Rate","Total RBC","(PCV)","Platelet Count"," Leucocytes Count","TSH (Thyroid Stimulating Hormone)","Glucose (Random)","Bilirubin Total","PH","WBC")
kidney=("Cretin level","Protein")
stroke=("BP (diastolic)","BP (systolic)","Pulse Rate")
liver=("Bilirubin Total","Bilirubin Direct","Bilirubin Indirect")
diabetes=("Glucose (Random)")


# In[9]:


#taking the disease as input
disease=input("Enter The disease whose report you are uploading:-")


# In[19]:


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

    j=1
    TEXT=""
    while j<i:
        fileimg = nm+str(j)+'.jpg'
        print(fileimg+" Scanned Successfully")
        img=cv2.imread(fileimg)
        text=pytesseract.image_to_string(img)
        TEXT=TEXT+text
        j=j+1

    print(TEXT)



    for i in vitals:
        spl_word = i
        if (TEXT.find(spl_word)!=-1):
            res=TEXT.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            if re.match('\d*\.?\d+',string):
                data.append(string)
            else:
                data.append('0')
        else:
            data.append('0')

    if disease=="Kidney" or disease=='kidney':
        for i in kidney:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')

    elif disease=="Stroke" or disease=="stroke":
        for i in stroke:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')
    elif disease=="Liver" or disease=="liver":
        for i in liver:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')
    elif disease=='Diabetes' or disease=='diabetes':
        for i in diabetes:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')


    return data



# In[20]:


def imgocr(file,disease):
    text=pytesseract.image_to_string(Image.open(file))
    print(text)

    TEXT=text

    for i in vitals:
        spl_word = i
        if (TEXT.find(spl_word)!=-1):
            res=TEXT.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            if re.match('\d*\.?\d+',string):
                data.append(string)
            else:
                data.append('0')
        else:
            data.append('0')

    if disease=="Kidney" or disease=='kidney':
        for i in kidney:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')

    elif disease=="Stroke" or disease=="stroke":
        for i in stroke:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')
    elif disease=="Liver" or disease=="liver":
        for i in liver:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')
    elif disease=='Diabetes' or disease=='diabetes':
        for i in diabetes:
            spl_word=i
            if (TEXT.find(spl_word)!=-1):
                res=text.partition(spl_word)[-1]
                res=res.split()
                string=res[0]
                if re.match('\d*\.?\d+',string):
                    data.append(string)
                else:
                    data.append('0')
            else:
                data.append('0')


    return data


# In[24]:


#Upload the file

    file=input("Enter the file name= ")

    expand=file.split(".")

    data=[]

    if expand[1]=="pdf":
        data=pdfocr(file,disease)

    else:
        data=imgocr(file,disease)






# In[ ]:

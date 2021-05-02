# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:20:23 2021

@author: ilker
"""

import os
from shutil import copy


def changeName(directory):
    workDirectory = directory + r'Augmented_Mel_Spectrograms-20210501T153934Z-001/Augmented_Mel_Spectrograms/Derivative_Augmentation_128_Order1/'
    for filename in os.listdir(workDirectory):
        os.rename(workDirectory + filename, workDirectory + 'derivativeAug128_order1_' + filename)



def setClassDirectory(directory):
    directory = directory + 'BPDatasetV3/'
    workDirectory = directory + r'MelSpectrogram_128/Unclassified/MelSpectrogramOriginal_Mel128'
    classDirectory = directory + r'MelSpectrogram_128/Divided Classes/MelSpectrogramOriginal_Mel128'

    for filename in os.listdir(workDirectory):
        splitted = filename.split('_')
        
        if splitted[len(splitted)-2] == '01':
            copy(workDirectory + '/' + filename, classDirectory + '/01-neutral')
        elif splitted[len(splitted)-2] == '02':
            copy(workDirectory + '/' + filename, classDirectory + '/02-calm')
        elif splitted[len(splitted)-2] == '03':
            copy(workDirectory + '/' + filename, classDirectory + '/03-happy')
        elif splitted[len(splitted)-2] == '04':
            copy(workDirectory + '/' + filename, classDirectory + '/04-sad')
        elif splitted[len(splitted)-2] == '05':
            copy(workDirectory + '/' + filename, classDirectory + '/05-angry')
        elif splitted[len(splitted)-2] == '06':
            copy(workDirectory + '/' + filename, classDirectory + '/06-fearful')
        elif splitted[len(splitted)-2] == '07':
            copy(workDirectory + '/' + filename, classDirectory + '/07-disgust')
        elif splitted[len(splitted)-2] == '08':
            copy(workDirectory + '/' + filename, classDirectory + '/08-surprised')
        else:
            print('Bir sorun var, boyle bir duygu yok!')
            



    
#Emotions (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised) 

#Main
directory = 'C:/Users/ilker/Desktop/Bp_datasetV3/'
#changeName(directory)    
setClassDirectory(directory)

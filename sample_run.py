import numpy as np
import pandas as pd
from pandas import read_csv
import cv2
import os
from symbolClassifier import symbolClassifier
import pickle

# load image as a numpy array im
im = cv2.imread("sample_symbol.png",0)
# initialize the classifier object
# models : 'svm', 'rf'
# func : 'test', 'train', 'validate'
sclf = symbolClassifier(model='svm',func='test')
# pass image as 2d numpy array to predict_class() method
# returns number label, name label and probability of the label
label, name, prob = sclf.predict_class(im)
# to get other probabilities : sclf.probabilities stores an array of all class probabilities for test image

print("Class : ", label,name)
print("Probability : ", prob)
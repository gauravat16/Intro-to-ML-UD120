#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()


time_before_fitting = time()

print features_train
print labels_train
classifier.fit(features_train,labels_train)
print "Time to fit",round(time()-time_before_fitting,3),"s"
time_before_prediction = time()
prediciton = classifier.predict(features_test)
print "Time to predict",round(time()-time_before_prediction,3),"s"

print classifier.score(features_test,labels_test)

#########################################################



#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
clf = SVC(kernel="rbf",C=10000)
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
time_before_fitting = time()
clf.fit(features_train, labels_train)
print "Time to fit", round(time() - time_before_fitting, 3), "s"

time_before_prediction = time()

pred = clf.predict(features_test)

# print pred[10]
# print pred[26]
# print pred[50]
print sum(pred)


print "Time to predict", round(time() - time_before_prediction, 3), "s"

acc = accuracy_score(pred, labels_test)
print acc



#########################################################

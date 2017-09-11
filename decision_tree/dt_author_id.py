#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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

from sklearn import tree
print len(features_train[0])
clf = tree.DecisionTreeClassifier(min_samples_split=40)

time_before_fitting = time()

clf.fit(features_train,labels_train)
print "Time to fit",round(time()-time_before_fitting,3),"s"
time_before_prediction = time()
prediction = clf.predict(features_test)
print "Time to predict",round(time()-time_before_prediction,3),"s"

acc = clf.score(features_test,labels_test)
print acc
#########################################################



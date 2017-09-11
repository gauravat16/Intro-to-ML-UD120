#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
sort_keys = '../tools/python2_lesson14_keys.pkl'




### your code goes here 



from sklearn import tree
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

from sklearn.model_selection import train_test_split

clf = tree.DecisionTreeClassifier()
features_train, features_test, labels_train, labels_test = train_test_split( features, labels, test_size=0.30, random_state=42)
clf.fit(features_train,labels_train)
print clf.score(features_test,labels_test)


print len(labels_test)

print
res = []
for i in range(0,29):
    # print clf.predict(features_test[i])
    # print i
    # print features_test[i]
    res.append(clf.predict(features_test[i]))

print precision_score(labels_test,res)
print recall_score(labels_test,res)
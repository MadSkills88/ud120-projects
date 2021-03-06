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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

from sklearn.svm import SVC
clf = SVC(C=10000, kernel="rbf")
t0 = time()
clf.fit (features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
labels_pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_pred, labels_test)
print accuracy

# answer1 = labels_pred[10]
# print answer1
# answer2 = labels_pred[26]
# print answer2
# answer3 = labels_pred[50]
# print answer3
count = 0
for prediction in labels_pred:
    if prediction == 1: count += 1
print count

#########################################################



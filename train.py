import os.path
import sys
import cv2
import utils
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cross_validation import cross_val_score
from sklearn import svm
from skimage.feature import hog

tmp = cv2.imread('staticmap.png', 0)
folder = 'yes'
labels = list()
features = list()
print cv2.__version__
detector = cv2.FeatureDetector_create("SURF")
descriptor = cv2.DescriptorExtractor_create("SURF")
count = 0
for f in os.listdir('yes'):
	count = count + 1
	labels.append(1)
	img = cv2.imread('yes/' + f, 0)
	features.append(hog(img))
	print 'yes/' + f
	print 'processed up to image ' + str(count)
for f in os.listdir('no'):
	count = count + 1
	labels.append(0)
	img = cv2.imread('no/' + f, 0)
	features.append(hog(img))
	print 'no/' + f
	print 'processed up to image ' + str(count)
print 'on to training'
clf = svm.SVC().fit(features, labels)
print cross_val_score(clf, features, labels, cv=5)
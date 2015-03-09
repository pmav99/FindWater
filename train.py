# Adding OpenCV to sys.path
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import os.path
import cv2
import utils
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cross_validation import cross_val_score
from sklearn import svm
from skimage.feature import hog
from PIL import Image

tmp = cv2.imread('staticmap.png', 0)
folder = 'yes'
labels = list()
features = list()
print cv2.__version__
detector = cv2.FeatureDetector_create("SURF")
descriptor = cv2.DescriptorExtractor_create("SURF")
count = 0
for f in os.listdir('yesNeal'):
	count = count + 1
	labels.append(1)
	img = cv2.imread('yesNeal/' + f, 0)
	print Image.open('yesNeal/' + f).size
	currFeatures = hog(img)
	print currFeatures
	print currFeatures.size
	features.append(currFeatures)
	#features.append(hog(img,normalise=True))
	print 'yes/' + f
	print 'processed up to image ' + str(count) + ' in "yes" folder'
print len(features)


#count = 0
#for f in os.listdir('no'):
#	count = count + 1
#	labels.append(0)
#	img = cv2.imread('no/' + f, 0)
#	features.append(hog(img,normalise=True))
#	print 'no/' + f
#	print 'processed up to image ' + str(count) + ' in "no" folder'


#print 'on to training'
#clf = svm.SVC().fit(features, labels)
#print cross_val_score(clf, features, labels, cv=5)

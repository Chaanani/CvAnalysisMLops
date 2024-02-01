import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics





def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

def cleaned_resume(Data):

    Data['cleaned_resume'] = Data.Resume.apply(lambda x: cleanResume(x))
    return Data


def label_coding(Data):

    var_mod = ['Category']
    le = LabelEncoder()
    for i in var_mod:
        Data[i] = le.fit_transform(Data[i])

    with open('../pickle/labelcoding.pkl', 'wb') as fichier:
         pickle.dump(le, fichier)
    return Data

def toknizer_text(Data):

    requiredText = Data['cleaned_resume'].values
    requiredTarget = Data['Category'].values
    word_vectorizer = TfidfVectorizer( sublinear_tf=True, stop_words='english', max_features=1500)
    word_vectorizer.fit(requiredText)
    WordFeatures = word_vectorizer.transform(requiredText)
    X_train, y_train = WordFeatures,requiredTarget
    
    with open('../pickle/word_vectorizer.pkl', 'wb') as fichier:
         pickle.dump(word_vectorizer, fichier)

    return X_train, y_train


def model_kpp(X_train, y_train):
    clf = OneVsRestClassifier(KNeighborsClassifier())
    clf.fit(X_train, y_train)
   
    with open('../pickle/model.pkl', 'wb') as fichier:
         pickle.dump(clf, fichier)







from data_processing import cleanResume, cleaned_resume, label_coding, toknizer_text

import pandas as pd

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



def train_model():
    Data = pd.read_csv('../datasets/UpdatedResumeDataSet.csv' ,encoding='utf-8')
    Data = cleaned_resume(Data)
    Data = label_coding(Data)
    X_train, y_train = toknizer_text(Data)
    clf = OneVsRestClassifier(KNeighborsClassifier())
    clf.fit(X_train, y_train)
   
    with open('../pickle/model.pkl', 'wb') as fichier:
         pickle.dump(clf, fichier)


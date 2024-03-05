import pickle
import pandas as pd
import sys
import sys
sys.path.append(r'C:\Users\msi\Desktop\Projects Github\Project_MLops')
from src.model.data_processing import cleanResume, cleaned_resume, label_coding, toknizer_text
import sys
import os

##sys.path.append(os.path.abspath('../../'))


def read_data():

    with open('../src/datasets/data.pickle', 'rb') as fichier:
         data_trained= pickle.load(fichier)
    data_new = pd.read_csv('../src/datasets/UpdatedResumeDataSet.csv' ,encoding='utf-8')
    
    return data_trained, data_new

def cleaning_data():


    data_trained, data_new = read_data()

    #### data_new
    data_new = cleaned_resume(data_new)
    requiredText_new = data_new['cleaned_resume'].values

    with open('../src/pickle/word_vectorizer.pkl', 'rb') as fichier:
         word_vectorizer = pickle.load(fichier)
    with open('../src/pickle/labelcoding.pkl', 'rb') as fichier:
         labelcoding = pickle.load(fichier)


    
    data_new["Category"] = labelcoding.transform(data_new["Category"])

    WordFeatures_new = word_vectorizer.transform(requiredText_new)
    requiredTarget_new = data_new['Category'].values

    #### data_trained
    

    data_trained = cleaned_resume(data_trained)
    requiredText_trained = data_trained['cleaned_resume'].values



    
    data_trained["Category"] = labelcoding.transform(data_trained["Category"])

    WordFeatures_trained = word_vectorizer.transform(requiredText_trained)
    requiredTarget_trained = data_trained['Category'].values
    

    return ( WordFeatures_trained, requiredTarget_trained ), ( WordFeatures_new, requiredTarget_new )

   
   
cleaning_data()


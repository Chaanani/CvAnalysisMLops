
import pickle
import pandas as pd
from src.model.data_processing import cleanResume, cleaned_resume, label_coding, toknizer_text
import sys
import os
#sys.path.append(os.path.abspath('../'))


def read_data():

    with open('src/datasets/data.pickle', 'rb') as fichier:
         data_trained= pickle.load(fichier)
    data_new = pd.read_csv('src/datasets/UpdatedResumeDataSet.csv' ,encoding='utf-8')
    
    return data_trained, data_new







#if __name__ == '__main__':
 #   app.run(debug=True)
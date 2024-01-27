import unittest
import pickle
import numpy as np
import re 
from sklearn.metrics import accuracy_score

with open('../pickle/labelcoding.pkl', 'rb') as fichier:
    labelcoding = pickle.load(fichier)
with open('../pickle/model.pkl', 'rb') as fichier:
    modele = pickle.load(fichier)
with open('../pickle/word_vectorizer.pkl', 'rb') as fichier:
    word_vectorizer = pickle.load(fichier)


def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText



class TestVotreModele(unittest.TestCase):

    def __init__(self,  methodName='runTest'):

        super().__init__(methodName)
        self.modele = modele
        self.feauture_test = ["Data Science,Skills â¢ R â¢ Python â¢ SAP HANA â¢ Tableau â¢ SAP HANA SQL","financial reports to respective departments. Reporting also included forecasting expenses.","Project Name: Consumption Based Planning for Flowers Foods Consultant; 8 months.The project involved setting up of CRM and CBP modules. Role:was involved in key data decomposition activities and setting up the base for future year"]
        self.label_test =["SAP Developer","Data Science","Data Science"]
 
    def test_prediction_long(self):
        
        clean_feauture = [cleanResume(resume) for resume in self.feauture_test]
        feature_TF_Idf = word_vectorizer.transform(clean_feauture) 
        prediction = self.modele.predict(feature_TF_Idf)
        self.assertEqual(len(prediction), len(self.label_test))  

    def test_prediction_class(self):

        clean_feauture = [cleanResume(resume) for resume in self.feauture_test]
        feature_TF_Idf = word_vectorizer.transform(clean_feauture) 
        prediction = self.modele.predict(feature_TF_Idf)
        predict_class =labelcoding.inverse_transform(prediction)

        self.assertEqual(list(predict_class), self.label_test)
        
    def test_performance(self):

        clean_feauture = [cleanResume(resume) for resume in self.feauture_test]
        feature_TF_Idf = word_vectorizer.transform(clean_feauture) 
        perdict_label = self.modele.predict(feature_TF_Idf)
        label_test =labelcoding.transform(self.label_test)

        performance = accuracy_score(label_test, perdict_label)

        print(performance)
        self.assertGreater(performance, 2, "La performance du modèle est inférieure au seuil acceptable.")

if __name__ == '__main__':
    unittest.main()
  

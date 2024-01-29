import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import re


st.title('CV  ')



with open('src/pickle/labelcoding.pkl', 'rb') as fichier:
    labelcoding = pickle.load(fichier)
with open('src/pickle/model.pkl', 'rb') as fichier:
    modele = pickle.load(fichier)
with open('src/pickle/word_vectorizer.pkl', 'rb') as fichier:
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


with st.form(key='my_form'):
    nom = st.text_input(label='Entrez le nom du condidat')
    age = st.text_input(label='Entrez le prénom du condidat')

    grand_texte = st.text_area(label='Entrez la résumé du CV ', height=300)
    submit_button = st.form_submit_button(label='Soumettre')

if submit_button:
    resume = cleanResume(grand_texte)
    resume = word_vectorizer.transform([resume])
    predict = modele.predict(resume)
    predicted_category_label = labelcoding.inverse_transform(predict)

    st.write("Catégorie prédite pour le nouveau CV :", predicted_category_label[0])

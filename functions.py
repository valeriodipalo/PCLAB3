import re
import spacy
nlp = spacy.load('en_core_web_sm')
import nltk
from nltk.corpus import stopwords

def word_count_col(df, text, new_col_name):
    """This function will define the number of words in each row of the considered dataframe
    df: dataframe to use
    text: the text column in the dataframe
    new_col_name: the name to which associate the column of word count"""
    tot = len(df)
    words = []
    for i in range(tot):
        words.append(len(df[text][i].split()))
    df[new_col_name] = words
    return df

def preprocess(input_text):
    """This function will allow us to perform all the preprocessing steps to reduce noise in text data. This is fundamental to perform text analysis.
    The function will return a list of cleaned sentences"""

    # Normalize to lowercase
    txt = input_text.lower()

    # Remove URLs
    txt = re.sub('https?://\S+|www\.\S+', '', txt)

    # Remove numbers
    txt = re.sub(r"\d", "", txt)

    # Remove punctuation
    txt = re.sub('\n', '', txt)
    txt = re.sub(r"[^A-Za-z]+", " ", txt)

    # Remove stopwords
    stop_words = [w.lower() for w in stopwords.words('english')]
    stop_words = set(stop_words).difference(set(['against','above','below', 'over', 'under']))
    txt = ' '.join([w for w in txt.split() if w not in stop_words and w !='user'])

    # Lemmatization
    lemmas = [token.lemma_ for token in nlp(txt)]
    txt = " ".join(lemmas)

    return txt


import tensorflow

import streamlit as st
import nltk
from nltk import sent_tokenize, word_tokenize, PorterStemmer
from nltk.corpus import stopwords

def summarize(document):
    # preprocess the document
    tokens = nltk.word_tokenize(document)
    # create a word frequency dictionary
    word_frequencies = {}
    for word in tokens:
        if word not in nltk.corpus.stopwords.words('english'):
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    maximum_frequency = max(word_frequencies.values())
    # divide word frequencies by maximum frequency to normalize
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/maximum_frequency
    # create a sentence score dictionary
    sentence_scores = {}
    for sent in nltk.sent_tokenize(document):
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
    # return a summary of the document using the top scoring sentences
    summary_sentences = nltk.sent_tokenize(document)[:3]
    return ' '.join(summary_sentences)

st.title('Document Summarization')

document = st.file_uploader("Pick a file")
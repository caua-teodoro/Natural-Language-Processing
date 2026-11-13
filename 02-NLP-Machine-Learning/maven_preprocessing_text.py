# import necessaries library
import pandas as pd
import spacy

# load the spacy model
nlp = spacy.load('en_core_web_sm')

# helper functions from text preprocessing section
def lower_remove(series):
    output = series.str.lower()
    output = output.str.replace(r'\[.*?\]', '', regex=True)
    output = output.str.replace(r'[^\w\s]', '', regex=True)
    return output

def token_lemma_nonstop(text):
    doc = nlp(text)
    output = [token.lemma_ for token in doc if not token.is_stop]
    return ' '.join(output)

def clean_and_normalize(series):
    output = lower_remove(series)
    output = output.apply(token_lemma_nonstop)
    return output

if __name__ == "__main__":
    print("Text Preprocessing module ready to use.")
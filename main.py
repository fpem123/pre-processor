'''
    Name: main.py
    Writer: Hoseop Lee, Ainizer
    Rule: Flask app
    update: 21.02.22
'''
# external module
from flask import Flask, request, jsonify, render_template, send_file, Response
import contractions
import unidecode
import spacy
from nltk.stem import WordNetLemmatizer

import os
import re


app = Flask(__name__)

UPLOAD_FOLDER = './data/upload'
RESULT_FOLDER = './data/result'

nlp = spacy.load('en_core_web_sm')  # spacy model load

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

if not os.path.isdir(RESULT_FOLDER):
    os.mkdir(RESULT_FOLDER)


##
# String to capitalize
def to_capitalize(text):
    result = text.capitalize()

    return result


##
# String to lower
def to_lower(text):
    result = text.lower()

    return result


##
# remove accent
# à -> a
def accent(text):
    result = unidecode.unidecode(text)

    return result


##
# Expand the abbreviation.
# ex) can't => can not
def expander(text):
    result = contractions.fix(text)

    return result


##
# short string remover
def short_remover(text, size):
    if len(text) <= size:
        return False

    return True


##
# Lemmatizer
# ex) bats -> bat, doing -> do
def lemmatizer(text):
    doc = nlp(text)
    tokens = []

    # make lemmatize token
    for token in doc:
        tokens.append(token)

    lemmatized_sentence = " ".join([token.lemma_ for token in doc])

    return lemmatized_sentence


##
# Reduce whitespace to one
# ex) Hello,  guy -> Hello, guy
def space_normalizer(text):
    result = " ".join(text.split())

    return result


##
# normalize full stop
# ex) This is Kim; And me. -> This is Kim. And me.
def full_stop_normalizer(text, stops):
    text:str
    stops = '[' + stops + ']'

    result = re.sub(stops, ".", text)

    return result


##
# normalize comma
# ex) This is Kim: and he is my son. -> This is Kim, and he is my son.
def comma_normalizer(text, stops):
    text:str
    stops = '[' + stops + ']'

    result = re.sub(stops, ",", text)

    return result


@app.route('/processor')
def processor():

    return


##
# Sever health checking page.
@app.route('/healthz', methods=["GET"])
def health_check():
    return "Health", 200


##
# Main page.
@app.route('/')
def main():
    return render_template('main.html'), 200


if __name__ == '__main__':
    from waitress import serve
    serve(app, port=80, host='0.0.0.0')
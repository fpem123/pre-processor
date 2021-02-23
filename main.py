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
from num2words import num2words

# internal module
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
def short_line_remover(text, size):
    if len(text) <= size:
        return False

    return True


##
# short word remover
def short_word_remover(text, size):
    rule = r'\W*\b\w{1,' + str(size) + r'}\b'
    shortword = re.compile(rule)

    result = shortword.sub('', text)

    return result


##
# special character remover
def special_remover(text, special):
    special = '[' + special + ']'

    result = re.sub(special, " ", text)

    return result


##
# special character remover
def special_replacer(text, specials):
    text: str

    for special in specials:
        text = text.replace(special[0], special[1])

    return text


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
# ex) Hello,    guy -> Hello, guy
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


##
# number to word
# ex) He is 3 years-old. -> He is three years-old.
def number_changer(text):
    text = text.split

    for idx in range(len(text)):
        if text[idx].isdecimal():
            text[idx] = num2words(text[idx])

    result = " ".join(text)

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
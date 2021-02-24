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
from werkzeug.utils import secure_filename
from threading import Thread
from queue import Queue, Empty
import time
import os
import re


app = Flask(__name__)

requests_queue = Queue()
BATCH_SIZE = 1
CHECK_INTERVAL = 0.1

UPLOAD_FOLDER = './data/upload'
RESULT_FOLDER = './data/result'

nlp = spacy.load('en_core_web_sm')  # spacy model load

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

if not os.path.isdir(RESULT_FOLDER):
    os.mkdir(RESULT_FOLDER)




def handle_requests_by_batch():
    while True:
        request_batch = []

        while not (len(request_batch) >= BATCH_SIZE):
            try:
                request_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
            except Empty:
                continue

            for requests in request_batch:

                try:
                    requests["output"] = transform(requests['input'][0], requests['input'][1])
                except Exception as e:
                    requests["output"] = e


handler = Thread(target=handle_requests_by_batch).start()


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
# emoji remover
def emoji_remover(text):
    result = text.encode('ascii', 'ignore').decode('ascii')

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


def transform(file, options):
    # 파일 저장
    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_path)

    result_path = os.path.join(RESULT_FOLDER, filename)

    print(options)

    try:
        with open(input_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()

            for option in options:
                print(option)
                pass

    except:
        pass

    os.remove(input_path)
    os.remove(result_path)

    return 0


def option_transform(options):
    options = options.split(",")

    return options


@app.route('/dpp', methods=['POST'])
def processor():
    try:
        if requests_queue.qsize() > BATCH_SIZE:
            return jsonify({'Error': 'Too Many Requests'}), 429

        args = []

        text_file = request.files['text_file']
        options = request.form.getlist('options')

        args.append(text_file)
        args.append(options)

    except Exception as e:
        return jsonify({'error': e}), 400

    req = {"input": args}
    requests_queue.put(req)

    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)

    result = req['output']

    if result:
        return
        #return send_file(result[0], mimetype='text/plain', attachment_filename=result[1]), 200
    else:
        return result


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
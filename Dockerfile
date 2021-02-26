FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime
FROM python

RUN pip install --upgrade pip

RUN pip install num2words \
    waitress \
    Unidecode \
    contractions \
    flask

# spacy module and spacy model download
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy[cuda102]
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
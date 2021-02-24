FROM python3

RUN pip install --upgrade pip

RUN pip install num2words \
    waitress \
    Unidecode \
    contractions \
    flask

RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
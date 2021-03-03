# Dockerfile CPU
FROM python

RUN pip install --upgrade pip

RUN pip install num2words \
    waitress \
    Unidecode \
    contractions \
    flask \
    emoji \
    torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# spacy module and spacy model download
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

RUN apt-get update && \
    apt-get install -y && \
    apt-get install -y apt-utils wget

RUN pip install --upgrade pip
RUN pip install num2words
RUN pip install waitress
RUN pip install Unidecode
RUN pip install contractions
RUN pip install flask

# spacy module and spacy model download
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy[cuda102]
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
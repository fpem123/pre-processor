FROM pytorch/pytorch:1.5.1-cuda10.1-cudnn7-runtime

RUN pip install --upgrade pip
RUN pip install num2words && \
    pip install waitress && \
    pip install Unidecode && \
    pip install flask

RUN pip install pyahocorasick==1.4.0
RUN pip install contractions

# spacy module and spacy model download
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy[cuda102]
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
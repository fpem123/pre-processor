FROM python

WORKDIR /dir

RUN pip install --upgrade pip
RUN pip install num2words && \
    pip install waitress && \
    pip install Unidecode && \
    pip install flask && \
    pip install contractions

FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

COPY --from=0 /dir .

# spacy module and spacy model download
RUN pip install -U pip setuptools wheel
# cuda 101 == cuda 10.1
RUN pip install -U spacy[cuda101]
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
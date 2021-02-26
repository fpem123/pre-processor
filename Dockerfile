FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3.6 python3.6-dev python3-pip python3-setuptools python3-wheel gcc

RUN pip install --upgrade pip
RUN pip install num2words && \
    pip install waitress && \
    pip install Unidecode && \
    pip install flask && \
    pip install contractions && \
    pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

# spacy module and spacy model download
RUN pip install -U pip setuptools wheel
# cuda 101 == cuda 10.1
RUN pip install -U spacy[cuda101]
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
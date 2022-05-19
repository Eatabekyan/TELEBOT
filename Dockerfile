FROM python:3.9-slim as compiler
ENV PYTHONUNBUFFERED 1


RUN python3 -m venv venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt requirements.txt
COPY ./telebot.py telebot.py
COPY ./parsingpart.py parsingpart.py
RUN pip3 install -Ur requirements.txt

CMD python3 telebot.py

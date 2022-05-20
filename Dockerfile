FROM python:3.9-slim as compiler
ENV PYTHONUNBUFFERED 1


RUN python3 -m venv venv
# Enable venv
ARG TOKEN
ENV PATH="/opt/venv/bin:$PATH"
ENV BOT_TOKEN=$TOKEN

COPY . .
RUN pip3 install -Ur requirements.txt

CMD python3 telebot.py

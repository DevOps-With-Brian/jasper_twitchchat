FROM python:3.11.1-alpine

WORKDIR /app

ENV TOKEN=""
ENV CLIENT_ID=""
ENV BOT_PREFIX="!"
ENV CHANNEL=""
ENV RASA_URL=""

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY bot.py .

CMD ["python3", "-m", "bot.py"]

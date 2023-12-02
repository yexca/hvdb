FROM python:3.11-alpine
RUN pip install requests \
    && pip install pyTelegramBotAPI

COPY ./inform.py /app/inform.py
CMD [ "python", "/app/inform.py" ]
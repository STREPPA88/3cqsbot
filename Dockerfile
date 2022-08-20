FROM python:3.9.10-slim

COPY . /App/
RUN pip install -r /App/requirements.txt 
RUN chmod +x /App/3cqsbot.py

WORKDIR /App

ENTRYPOINT ["./start.sh", ""]
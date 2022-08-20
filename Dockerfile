FROM python:3.9.10-slim

COPY . /App/
RUN pip install -r /App/requirements.txt 
RUN chmod +x /App/3cqsbot.py

WORKDIR /App

ENTRYPOINT ["python3", "./importconfig.py", "--host=0.0.0.0", "port=$PORT"]
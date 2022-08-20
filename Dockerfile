FROM python:3.9.10-slim

COPY . /App/
RUN pip install -r /App/requirements.txt 
RUN chmod +x /App/3cqsbot.py
#RUN chmod-R 777 /usr/local/lib/python3.9/site-packages/telethon/client/
#ADD /usr/local/lib/python3.9/site-packages/telethon/sessions/ /App/

WORKDIR /App

ENTRYPOINT ["python3", "./importconfig.py", "0.0.0.0"]
FROM python:latest

COPY status_state_api.py requirements.txt /

RUN apt update && apt install -y python3 python3-pip
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python ./status_state_api.py

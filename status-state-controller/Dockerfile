FROM python:latest

COPY status_state_controller.py requirements.txt /

RUN apt update && apt install -y python3 python3-pip tmux
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python ./status_state_controller.py

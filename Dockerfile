FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /websocket_server
WORKDIR /websocket_server
ADD requirements.txt /websocket_server/
RUN pip install -r requirements.txt
ADD . /websocket_server/

CMD [ "python", "-u", "./index.py" ]
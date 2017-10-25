FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /application
 WORKDIR /application
 ADD requirements.txt /application/
 ADD docker-entrypoint.sh /application/
 RUN pip install -r requirements.txt
 ADD . /application/

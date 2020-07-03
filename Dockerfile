FROM python:3.7
WORKDIR /usr/url_service
ADD requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "shorten.py" ]
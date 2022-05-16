FROM python:3.8
LABEL maintainer="Joe Chien"

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["python", "app/main.py"]

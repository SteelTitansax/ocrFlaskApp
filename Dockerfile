FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev build-essential
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tesseract-ocr
COPY / /app/
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["main.py"]

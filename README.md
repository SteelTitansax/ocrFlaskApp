# Ocr Reader MPL

This is an exercise for create a flask app with an OCR system integrated, dockerize it and deploy it in an Azure App Service

## Deployment instructions

sudo docker build -t ocrapiflaskimage .

sudo docker login <containername>.azurecr.io --username <containerUserName> --password <password>

sudo docker tag ocrapiflaskimage <containername>.azurecr.io/ocrapiflaskimage:v1

sudo docker push <containername>.azurecr.io/ocrapiflaskimage:v1


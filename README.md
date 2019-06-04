# macinfo_docker_img
Get Mac info from https://macaddress.io api request

# app.py
This code uses urllib python library to call macaddress.ip restfull api.

# Building image.
Image build specification is written in Dockerfile and have entrypoint script called macaddr.
macaddr script will pass two paramter to app.py which is mac address and API_KEY
Following command is used to build the image

**docker build --tag=macinfo .**
- Sending build context to Docker daemon  69.63kB

- Step 1/5 : FROM python:3.6-slim
- Step 2/5 : WORKDIR /app
- Step 3/5 : COPY app.py /app
- Step 4/5 : COPY macaddr /app
- Step 5/5 : ENTRYPOINT ["/app/macaddr"]
- Successfully built 5d0dd17c6b9b
- Successfully tagged macinfo:latest

# Running Image.

Following command is used to run the . API_KEY can be obtained by signing up at macaddress.io website.

**docker run -e API_KEY=xxxxxxxxx macinfo 44:38:39:ff:ef:57**
MAC_ADDRESS=44:38:39:ff:ef:57,COMPANY_NAME=Cumulus Networks, Inc



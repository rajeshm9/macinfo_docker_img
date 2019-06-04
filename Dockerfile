FROM python:3.6-slim
WORKDIR /app
COPY app.py /app
COPY macaddr /app
#CMD ["python","app.py"]
ENTRYPOINT ["/app/macaddr"]

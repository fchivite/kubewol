FROM python:3.12-alpine
RUN pip install flask
WORKDIR /web
COPY kubewol.py .
ENTRYPOINT ["python", "kubewol.py"]

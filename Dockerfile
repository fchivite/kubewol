FROM python:3.12-alpine
RUN pip install flask
RUN pip install wakeonlan
WORKDIR /web
COPY kubewol.py .
ENTRYPOINT ["python", "kubewol.py"]

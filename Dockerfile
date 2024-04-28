FROM python:3.12-alpine
RUN pip install flask flask_sqlalchemy wakeonlan pythonping flask-apscheduler
WORKDIR /kubewol
COPY kubewol.py .
COPY webconsole  webconsole/
ENTRYPOINT ["python", "kubewol.py"]

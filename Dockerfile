FROM python:3.9.4
RUN mkdir /app
RUN mkdir /app/code
ADD . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt
CMD ["python", "app.py"]


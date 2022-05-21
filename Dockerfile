FROM python:3.10

WORKDIR /app
COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
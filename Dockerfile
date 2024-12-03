FROM python:3.12.7

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --timeout=120

COPY . .

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_RUN_PORT=3000

EXPOSE 3000

CMD ["flask", "run"]
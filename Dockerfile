FROM python:3.12.7

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT 3000

EXPOSE 3000

CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]
FROM python:3.13.2-alpine3.21

WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg y compilaciones si las hubiera
RUN apk add --no-cache gcc musl-dev libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]

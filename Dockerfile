FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 2121

ENV FLASK_APP=app.py
ENV FLASK_ENV=environment

CMD ["flask", "run", "--host=0.0.0.0", "--port=2121"]


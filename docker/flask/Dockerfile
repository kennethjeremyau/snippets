FROM python:3.9.1-alpine3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ \
    "gunicorn", \
    "--bind", "0.0.0.0:80", \
    "--access-logfile", "-", \
    "--error-logfile", "-", \
    "server:app" \
]

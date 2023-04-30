FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app/app

RUN pip install -r /app/requirements.txt

EXPOSE 80

FROM python:3.9

COPY ./app /app/app

WORKDIR /app

RUN pip install fastapi uvicorn

EXPOSE 8090

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","15500"]
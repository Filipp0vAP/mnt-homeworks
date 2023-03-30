FROM python:alpine

EXPOSE 5290

WORKDIR /python_api

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY app.py ./

CMD ["python3", "app.py"]

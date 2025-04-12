FROM python:3.13.2
EXPOSE 5000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app
CMD ["flask", "run", "--host", "0.0.0.0"]

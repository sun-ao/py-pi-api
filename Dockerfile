FROM python:3.8

WORKDIR /app/

COPY Pipfile ./
RUN pip install -i https://mirrors.aliyun.com/pypi/simple pipenv
RUN pipenv run pipenv install

COPY . .

EXPOSE 8080

CMD [ "pipenv", "run", "python", "/app/main.py" ]
FROM python:3
LABEL maintainer="EMAIL"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
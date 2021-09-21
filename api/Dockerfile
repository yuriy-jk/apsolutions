FROM python:3.9

RUN apt update && apt -y install gettext-base
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
#CMD csvsql --db postgresql://user:pass@postgres:5432/posts_db --insert posts.csv
# CMD python main.py
# RUN csvsql --db postgresql://user:pass@postgres:5432/posts_db --insert posts.csv


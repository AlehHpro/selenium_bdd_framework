FROM joyzoursky/python-chromedriver:3.8

COPY . /selenium_bdd_framework

WORKDIR /selenium_bdd_framework

RUN pip3 install pipenv
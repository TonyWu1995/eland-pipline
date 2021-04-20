FROM python:3.8-slim

# Install pipenv
RUN pip install --upgrade pip==21.0.1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Workspace setup
COPY ./ ./
ENV PYTHONPATH "${PYTHONPATH}:/"

RUN pip install -r requirements/prod.txt

CMD ["python", "app.py","conf/application.yml","conf/config.json"]

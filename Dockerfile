FROM python:3.8

# Install pipenv
RUN pip install --upgrade pip==20.2.4
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Workspace setup
COPY ./ ./
ENV PYTHONPATH "${PYTHONPATH}:/"

RUN pip install -r requirements/prod.txt

CMD ["python", "app.py"]

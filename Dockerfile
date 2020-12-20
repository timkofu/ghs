
FROM python:3.9.1-buster

LABEL name="@timkofu"

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PRODUCTION 1

# copy project
COPY . .

# install dependencies
RUN pip install -U pip
RUN pip install --use-feature=2020-resolver -r requirements.txt

# add and run as non-root user
RUN useradd -ms /bin/bash ghs
USER ghs

# run uvicorn
CMD uvicorn ghs.view.web.endpoints:app --workers $WORKERS --host 0.0.0.0 --port $PORT --loop uvloop --http httptools --interface asgi3 --log-level info
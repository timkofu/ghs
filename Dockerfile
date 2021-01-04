
FROM python:3.9.1-buster

LABEL name="@timkofu"

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PRODUCTION 1
ENV NEW_RELIC_CONFIG_FILE=newrelic.ini 

# copy project
COPY . .

# install dependencies
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

# add and run as non-root user
RUN useradd -ms /bin/bash ghs
USER ghs

# run uvicorn
# ENTRYPOINT ["newrelic-admin", "run-program"]
# CMD ["uvicorn", "ghs.view.web.endpoints:app", "--workers 4", "--host 0.0.0.0", "--port $PORT", "--loop uvloop", "--http httptools", "--interface asgi3", "--log-level info"]
# That $PORT part won't get interpolated

# Use Alpine-based Python image
FROM python:3.12-alpine

# Copy the source code into the container.
COPY . /usr/src/app
WORKDIR /usr/src/app

#
RUN \
    apk add --no-cache python3 postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

EXPOSE 8080
# Command to run the application with automatic reload


CMD ["./entrypoint.sh"]

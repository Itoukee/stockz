# Use Alpine-based Python image
FROM python:3.12-alpine

# Copy the source code into the container.
COPY . /usr/src/app
WORKDIR /usr/src/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
# Command to run the application with automatic reload
CMD ["python","index.py"]

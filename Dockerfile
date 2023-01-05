FROM python:3.10.8

# Copy the program files
COPY fetch.py /app/fetch.py
COPY requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install the required libraries
RUN pip install -r requirements.txt

# Set the entry point to the program
ENTRYPOINT ["python", "fetch.py"]


# Base Image to build your image on
FROM python:3.10 AS base

# Set the working directory
WORKDIR /root/intro-to-container/container-a

# Copy the files from your directory into the image
COPY . .

# Install the specified dep onto the image
RUN pip3 install -r requirements.txt

# Execute Command
CMD ["python3", "main.py"]
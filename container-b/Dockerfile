ARG docker_user

FROM ${docker_user}/intro-to-container-a:latest

WORKDIR /root/intro-to-container/container-b

# Copy local file
COPY . .

# Install the specified dep onto the image
RUN pip3 install -r requirements.txt
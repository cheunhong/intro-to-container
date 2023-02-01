# Intro to Docker
## Slides
https://docs.google.com/presentation/d/1ZHYTt6uwt_oDOzt7WzODdw7P5VrmvzSjJRDf9o9oYCA/edit?usp=sharing

## Prequisite
1. Has `Docker Desktop` installed
2. Signup and login into `Docker Desktop` with personal account
3. export your account username as env variable
```bash
export DOCKER_USER={your_docker_username}
```

## Container A
Showcase the the `build` and `push` process

1. Building the image with tag
```bash
docker build -t $DOCKER_USER/intro-to-container-a .
```
2. Pushing the image to image registry
```bash
docker push $DOCKER_USER/intro-to-container-a
```

## Container A Clone
Showcase the the `pull` and `run` process

1. Pulling the image
```bash
docker pull $DOCKER_USER/intro-to-container-a
```
2. Running the image
```bash
docker run $DOCKER_USER/intro-to-container-a
```

## Container B
Showcase example of using custom image and pushing to private registry
1. Authenticate ECR
```bash
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 268437748782.dkr.ecr.ap-southeast-1.amazonaws.com
```
2. Building the image with tag
```bash
docker build --build-arg docker_user=$DOCKER_USER -t 268437748782.dkr.ecr.ap-southeast-1.amazonaws.com/intro-to-container-b .
```
3. Push to private registry
```bash
docker push 268437748782.dkr.ecr.ap-southeast-1.amazonaws.com/intro-to-container-b
```

## Container A with arguments
Showcase example of using volume mount and env using `docker run`
1. Run
```bash
docker run \
    -v $(pwd):/root/intro-to-container/container-a \
    -e ENV=staging \
    $DOCKER_USER/intro-to-container-a
```

## Docker Compose

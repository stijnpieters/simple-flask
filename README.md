# How to
## Docker
docker build -t webapp .

docker run -d --name flask-webapp --restart always -p 5000:5000 webapp:latest

## docker-compose
docker-compose up -d

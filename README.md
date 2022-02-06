# How to

```
git clone https://github.com/stijnpieters/simple-flask.git
```
Edit app.py with logic (e.g. to write to database)
additionally: add the required pip packages to requirements.txt

## Docker
```
docker build -t webapp .

docker run -d --name flask-webapp --restart always -p 5000:5000 webapp:latest
```
## docker-compose
```
docker-compose up -d
```

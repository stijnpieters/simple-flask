# How to

```
git clone https://github.com/stijnpieters/simple-flask.git
```
Edit app.py with logic (e.g. to write to database)

additionally: add the required pip packages to requirements.txt

create a file named .env in the root of this repo
add the following
| Variable Name | Description                     | Default |
|---------------|---------------------------------|---------|
| USERNAME      | Username to connect to influxdb | None    |
| PASSWORD      | password for influxdb           | None    |
| INFLUXHOST    | influx IP/hostname              | None    |
| INFLUXPORT    | influx port                     | None    |
| DATABASE      | database name                   | None    |

edit the data variable at line 25 to write to your desired measurement


## Docker
```
docker build -t webapp .

docker run -d --name flask-webapp --restart always -p 5000:5000 webapp:latest
```
## docker-compose
```
docker-compose up -d
```

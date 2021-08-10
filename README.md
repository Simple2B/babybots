# Instruction for deploy application

All script run logs will be in files:

- run-script.out
- run-script.err

How to get web application logs?

- use docker-compose command:

```bash
docker-compose logs -f
```

## Deploy from github

Choice or create folder for deploy. Go to the project folder and and download the project from GitHub [here](https://github.com/Simple2B/babybots):

```bash
cd ~/project_folder
git clone https://github.com/Simple2B/babybots.git .
```

## Prepare python virtual environment

Open a project and create python virtual environment:

```bash
cd ~/project_folder
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Create .env file

In the project folder need create file *.env* with next context:

```dotenv
SECRET_KEY=<<secret-key-string>>

ADMIN_USER_NAME=admin
ADMIN_USER_PASS=1234
```

> **_NOTE:_**  Please put here default admin credentials.

## Prepare database

Execute following lines under virtual environment

```bash
flask drob-db
flask create-db
```

## Docker

To build and run docker container:

```bash
docker-compose up --build -d
```

## Crontab

Crontab run script every minute

```bash
crontab -e
```

Write to file:

```crontab
* * * * *  path to run-script.sh
```

Read file:

```bash
crontab -l
```

## NGINX configuration

```nginx
server {
    server_name <<your DNS server name>>;
    location / {
      proxy_pass http://localhost:5000;
    }

    listen 80;
}
```

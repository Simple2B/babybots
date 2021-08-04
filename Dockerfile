FROM python:3.9

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN python -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY . .
# CMD flask create-db
# CMD flask run --host 0.0.0.0 --port 7785

EXPOSE 5000

### Run Docker

1. Run script for certs nginx
```
cd scripts
./generate_nginx_server_ssl.sh
```

2. Run: build docker image by using


create .env file on ./deployment/prod/.env

```
cd ./deployment/prod
nano .env

IMAGE_NAME = fr-api
VERSION = v0.0.1
```


```
cd face-verify
docker compose -f deployment/prod/docker-compose.build.yaml build
```

start service run this script
```
cd face-verify
docker compose -f deployment/prod/docker-compose.yaml up -d
```

### Branch Strategy

1. Branching strategy:
   - **main** 
   - **develop** 
   - **feature/{ feature-name in lowercase, dash separate }** 
   - **refactor/{ context in lowercase, dash separate }** 

2. Checkout new branch in context ex:
```
git checkout -b feature/new-feature
```



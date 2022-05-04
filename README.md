
- install necessary packages:

```
apt install docker.io python3 python3-pip
```

(depending on the system it might necessary to tweak the firewall settings or download the proper version of docker-compose and docker)

- clone git repository:

```
git clone https://github.com/calm-tedesco/devops-test
```

- run docker-compose:

```
sudo docker-compose up -d
```

Done! It should be up and running already.

There are two services: status_state_api and status_state_controller
status_state_api is listening for requests on port 8080 (/docker-ps):
http://status-state-api:8080/docker-ps from status_state_controller

We can execute the following commands to see that the setup works:

```
curl -v http://localhost:8080/docker-ps
docker logs -f status-state-controller
```

things to add with more time:
- kubernetes deployment, docker-compose does the job locally but can be translated into a kubernetes configuration
- addition of unit tests, pytests
- use of decorators to send information to elk stack

# Running on bigubu and docker

## Bigubu
Copy files to bigubu (for example over scp). Run _docker container ls_ to check if container is not already running and remove it with _docker stop [container name]_ and _docker rm [container name]_ if you want to run it by yourself. Always add 'z13_' prefix to container name and always use network 'z13_network'


## Build and run server container:
In server files directory, run:
```
docker build -t z13_serverpy .
docker run -dit --network-alias z13_serverpy --network z13_network --name z13_serverpy z13_serverpy 8001
```
You can also change the name of the container as long as you use 'z13_' prefix. 8001 is the port number, passed as a positional argument to the server program. This is also an example value that can change. The options will start the container in detached mode, which will allow you to run the client on the same terminal with the server running in the background.

## Build and run client container:
In client files directory, run:
```
docker build -t z13_clientpy .
docker run -it --network z13_network z13_clientpy z13_serverpy 8001
```
Client has 2 positional arguments: hostname and port. In this case, hostname is the network alias of the server container which will be resolved by docker's DNS. The port is the same to which the server has been configured.

## Check server logs:
```
docker logs --tail [number] --follow z13_serverpy
```
This command will show the last _/number/_ lines output by container z13_serverpy. This is an easy way to check what the server was outputting while running in the background.
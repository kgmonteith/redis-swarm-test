#!/usr/bin/env bash

# Assumes swarm has already been initialized
docker build --tag localhost:5000/populator -f populator-Dockerfile .
docker build --tag localhost:5000/monitor -f monitor-Dockerfile .
docker push localhost:5000/populator
docker push localhost:5000/monitor

docker network create --driver overlay test-network
docker service create --name redis --network test-network redis
docker service create --name populator --env TASKNAME=TEST --network test-network localhost:5000/populator
docker service create --name monitor --env TASKNAME=TEST --network test-network localhost:5000/monitor

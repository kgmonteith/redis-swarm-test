#!/usr/bin/env bash

# Assumes swarm has already been initialized
docker service rm populator monitor redis
docker network rm test-network
docker rmi localhost:5000/populator localhost:5000/monitor
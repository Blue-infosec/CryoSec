#!/bin/bash
docker rm lockdown
#docker build -t lockdown .
#docker run --name lockdown -t -i --rm docker.io/devmantillis/cryosec_lockdown ansible --version
#docker run --name lockdown -t -i --rm docker.io/devmantillis/cryosec_lockdown git --version
docker run --name lockdown -t -i --rm docker.io/devmantillis/cryosec_lockdown bash

#docker run --name lockdown docker.io/devmantillis/cryosec_lockdown
# Detached
#docker run --name lockdown -d docker.io/devmantillis/cryosec_lockdown

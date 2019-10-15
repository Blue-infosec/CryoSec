#!/bin/bash
#docker build -t lockdown .
docker run --name lockdown -t -i --rm docker.io/devmantillis/cryosec_lockdown ansible --version
docker run --name lockdown -t -i --rm docker.io/devmantillis/cryosec_lockdown git --version
docker run --name lockdown -t -i --rm docker.io/devmantillis/cryosec_lockdown bash

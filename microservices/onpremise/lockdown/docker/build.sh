#!/bin/bash
docker build -t cryosec_lockdown .
docker tag cryosec_lockdown:latest 096412041307.dkr.ecr.us-west-2.amazonaws.com/cryosec_lockdown:latest
docker push 096412041307.dkr.ecr.us-west-2.amazonaws.com/cryosec_lockdown:latest
docker build -t docker.io/devmantillis/cryosec_lockdown .
docker push devmantillis/cryosec_lockdown:latest

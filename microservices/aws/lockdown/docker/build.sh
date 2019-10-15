#!/bin/bash
docker build -t docker.io/devmantillis/cryosec_lockdown .
docker push devmantillis/cryosec_lockdown:latest

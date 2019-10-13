#!/bin/bash
#docker build -t lockdown .
docker run --name lockdown -t -i --rm lockdown ansible --version
docker run --name lockdown -t -i --rm lockdown git --version
docker run --name lockdown -t -i --rm lockdown bash

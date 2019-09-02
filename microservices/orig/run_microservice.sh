#!/bin/bash
#sudo setenforce 0

event=$(cat event.json)
docker run --rm -v "$PWD":/var/task lambci/lambda:python3.7 lambda_function.lambda_handler "$event"

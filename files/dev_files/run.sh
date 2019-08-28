#!/bin/bash
#sudo setenforce 0
docker run --rm -v "$PWD":/var/task lambci/lambda:python3.7 lambda_function.lambda_handler '{"some": "event"}'

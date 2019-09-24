#!/bin/bash

selinux_status=$(getenforce)
$event=$(cat QUERY_event.json)

function microservice(){
    ./create_stack "modify"

    docker run --rm -v "$BUILD":/var/task \
     lambci/lambda:python3.7 app.lambda_handler "$event"

}

function main(){
if [ "$selinux_status" = "Permissive" ]; then
    microservice
  else
    setenforce 0
    microservice
    setenforce 1
  fi
}

main

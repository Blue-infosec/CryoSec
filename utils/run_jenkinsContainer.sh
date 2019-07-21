#!/bin/bash
zdocker rm cryosec --force
zdocker run --name cryosec -v /mnt/c/Users/standard/Desktop/cryoSecSDK/CryoSec/files/jenkinsServerExport:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

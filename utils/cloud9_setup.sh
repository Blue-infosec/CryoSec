#!/bin/bash
yum update -y
yum groupinstall -y "Development Tools"
yum install -y \
  python3-devel \
  wget \
  zlib-devel \
  libffi-devel \
  openssl-devel \
  git
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
tar -xzf Python-3.7.4.tgz
cd Python-3.7.4
./configure
make
make altinstall
#/usr/local/bin/pip3.7 install virtualenv
#virtualenv cryosec
#. cryosec/bin/activate
#pip install 'ansible==2.8'

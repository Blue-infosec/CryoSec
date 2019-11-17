#!/bin/bash

# Install node
wget https://nodejs.org/dist/v12.13.0/node-v12.13.0-linux-x64.tar.xz
tar -xf node-v12.13.0-linux-x64.tar.xz
mv node-v12.13.0-linux-x64/bin/* /usr/local/bin/
rm -rf node-v12.13.0-linux-x64/
rm -rf node-v12.13.0-linux-x64.tar.xz
# node --version
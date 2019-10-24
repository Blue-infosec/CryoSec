#!/bin/bash
/usr/local/bin/pip3.7 install virtualenv --user
virtualenv cryosec_venv
. cryosec_venv/bin/activate
pip install 'ansible==2.8'

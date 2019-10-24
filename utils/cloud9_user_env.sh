#!/bin/bash
/usr/local/bin/pip3.7 install virtualenv --user
virtualenv cryosec_venv
. cryosec_venv/bin/activate
pip install 'ansible==2.8'
cat <<EOT >> /home/ec2-user/.bashrc
. /home/ec2-user/environment/cryosec_venv/bin/activate
cd /home/ec2-user/environment/CryoSec
echo "Updating CryoSec Repo..."
git pull
PATH=$PATH:/home/ec2-user/environment/CryoSec
EOT

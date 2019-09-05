#!/bin/bash
cd ../
ansible-playbook -i "localhost," -c local --check linux.yml -K

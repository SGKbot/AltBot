#!/bin/bash
docker system prune -f
docker build -t sgkond/altbot .
docker push sgkond/altbot
ansible-playbook -i ansible/hosts ansible/site.yaml -D
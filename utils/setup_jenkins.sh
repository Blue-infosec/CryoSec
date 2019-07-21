docker pull jenkins/jenkins:lts
/etc/init.d/docker start
docker pull jenkins/jenkins:lts
usermod -aG docker sysadmin
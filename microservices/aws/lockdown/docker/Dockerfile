FROM centos:7
RUN yum update -y
RUN yum groupinstall -y "Development Tools"
RUN yum install -y \
  python3-devel \
  wget \
  zlib-devel \
  libffi-devel \
  openssl-devel \
  git
RUN wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
RUN tar -xzf Python-3.7.4.tgz
WORKDIR Python-3.7.4
RUN pwd
RUN ls
RUN ./configure
RUN make
RUN make altinstall
RUN pip3.7 install 'ansible==2.8'
RUN mkdir /lockdown
RUN mkdir /root/.ssh/
WORKDIR /lockdown
COPY id_rsa /root/.ssh/id_rsa
COPY id_rsa.pub /root/.ssh/id_rsa.pub
RUN chmod -R 400 /root/.ssh/
RUN echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config
RUN git clone git@github.com:DevManTillis/CryoSec.git
WORKDIR /lockdown/CryoSec/microservices/aws/lockdown/ansible/
CMD /bin/bash -c "while true; do sleep 1000; done"

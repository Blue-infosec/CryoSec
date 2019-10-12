FROM centos:7
RUN yum update -y
RUN yum groupinstall -y "Development Tools"
RUN yum install -y \
  python3-devel \
  wget \
  zlib-devel \
  libffi-devel \
  openssl-devel
RUN wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
RUN tar -xzf Python-3.7.4.tgz
WORKDIR Python-3.7.4
RUN pwd
RUN ls
RUN ./configure
RUN make
RUN make altinstall
RUN pip3.7 install 'ansible==2.8'
